import apache_beam as beam 
from apache_beam.options.pipeline_options import PipelineOptions 
from beam_nuggets.io import relational_db

records = [
    {'name': 'May', 'num': 5},
    {'name': 'Jun', 'num': 6}
]

source_config = relational_db.SourceConfiguration(
    drivername='postgresql+pg8000',
    host='34.136.227.124',
    port=5432,
    username='postgres',
    password='Passw0rd1!',
    database='demodb',
    create_if_missing=True  # create the database if not there 
)

table_config = relational_db.TableConfiguration(
    name='months_col',
    create_if_missing=True,  # automatically create the table if not there
    primary_key_columns=['num']  # and use 'num' column as primary key
)
    
with beam.Pipeline(options=PipelineOptions()) as p:  # Will use local runner
    months = p | "Reading month records" >> beam.Create(records)
    months | 'Writing to DB' >> relational_db.Write(
        source_config=source_config,
        table_config=table_config
    )

if __name__ == '__main__':
	print("Data successfully migrated to Postgres!")