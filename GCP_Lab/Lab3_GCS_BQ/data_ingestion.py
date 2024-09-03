import apache_beam as beam 
import logging
import argparse
from apache_beam.options.pipeline_options import PipelineOptions
import re 

import os 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/sauravlearner1987/newproject2506-8cab1fae387d.json"

class DataIngestion:
	def parse_method(self, string_input):
		values = re.split(",", re.sub('\r\n', '', string_input))
		row = dict(
			zip(('state','gender','year','name','number','created_date'), values)
			)
		return row 

def run(argv=None):
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--input',
		dest='input',
		required=False,
		default='xc'
		)
	parser.add_argument(
		'--output',
		dest='output',
		required=False,
		default='lake.usa_names'
		)
	known_args, pipeline_args = parser.parse_known_args(argv)
	data_ingestion = DataIngestion()
	p = beam.Pipeline(options=PipelineOptions(pipeline_args))
	(p
		| 'Read from GCS' >> beam.io.ReadFromText(known_args.input, skip_header_lines=1)
		| 'String to BQ Row' >> beam.Map(lambda s: data_ingestion.parse_method(s))
		| 'Write to BQ' >> beam.io.Write(
			beam.io.BigQuerySink(
				known_args.output,
				schema='state:STRING,gender:STRING,year:STRING,name:STRING,number:STRING,created_date:STRING',
				create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
				write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
				))
		)
	p.run().wait_until_finish()

if __name__=='__main__':
	logging.getLogger().setLevel(logging.INFO)
	run()