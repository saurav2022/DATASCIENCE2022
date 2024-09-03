import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import argparse
from google.cloud import bigquery
from apache_beam.runners.runner import PipelineState

delivered_table_spec = "newproject2007.myds2024.survived_data"

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input", dest="input", required=True, help="Input file to process."
)
path_args, pipeline_args = parser.parse_known_args()
inputs_pattern = path_args.input

options = PipelineOptions(pipeline_args)
p = beam.Pipeline(options=options)


def remove_last_column(row):
    cols = row.split(",")
    item = str(cols[4])
    if item.endswith(":"):
        cols[4] = item[:-1]
    return ",".join(cols)


def print_row(row):
    print(row)


cleaned_data = (
    p
    | beam.io.ReadFromText(inputs_pattern, skip_header_lines=1)
    | beam.Map(remove_last_column)
    | beam.Map(lambda row: row.lower())
    | beam.Filter(lambda row: row.split(",")[1].lower() == "1")
    | beam.Map(lambda row: row + ",Titanic Survived")
)

survived_data = cleaned_data | "Filtering female passengers" >> beam.Filter(
    lambda row: row.split(",")[3].lower() == "female"
)

(
    survived_data
    | "count delivered" >> beam.combiners.Count.Globally()
    | "delivered map" >> beam.Map(lambda x: "Delivered count: " + str(x))
    | "print delivered count" >> beam.Map(print_row)
)

client = bigquery.Client()
dataset_id = f"{client.project}.myds2024"

try:
    client.get_dataset(dataset_id)
except:
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"
    dataset.description = "dataset for survived passengers in Titanic"
    dataset_ref = client.create_dataset(dataset, timeout=30)


def to_json(csv_str):
    fields = csv_str.split(",")
    json_str = {
        "PassengerId": fields[0],
        "Survived": fields[1],
        "Pclass": fields[2],
        "Sex": fields[3],
        "Age": fields[4],
        "SibSp": fields[5],
        "Parch": fields[6],
        "Ticket": fields[7],
        "Fare": fields[8],
        "Cabin": fields[9],
        "Embarked": fields[10],
        "Metadata": fields[11],
    }
    return json_str


table_schema = "PassengerId:STRING, Survived:STRING, Pclass:STRING, Sex:STRING, Age:STRING, SibSp:STRING, Parch:STRING, Ticket:STRING, Fare:STRING, Cabin:STRING, Embarked:STRING, Metadata:STRING"

(
    survived_data
    | "delivered to json" >> beam.Map(to_json)
    | "write delivered"
    >> beam.io.WriteToBigQuery(
        delivered_table_spec,
        schema=table_schema,
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
    )
)

ret = p.run()
if ret.state == PipelineState.DONE:
    print("Success!!!")
else:
    print("Error running beam pipeline")
