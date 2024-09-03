# Direct Runner
import argparse
import apache_beam as beam 
import logging 
from apache_beam.options.pipeline_options import PipelineOptions 
from apache_beam import window
from datetime import datetime as dt 

class AddWindowdtlsFn(beam.DoFn):
	def process(self, element, window=beam.DoFn.WindowParam):
		window_start = window.start.to_utc_datetime()
		window_end = window.end.to_utc_datetime()
		pc = str(element) + " [ " + str(window_start) + ' - ' + str(window_end) + " ]"
		pc.split('\n')
		yield pc

def run(input_topic, output_path, pipeline_args=None):
	pipeline_options = PipelineOptions(
		pipeline_args, streaming=True, save_main_session=True
		)
	with beam.Pipeline(options=pipeline_options) as p:
		(
			p
			| "Read event stream data from topic" >> beam.io.ReadFromPubSub(topic=input_topic)
			| "Convert from byte to string" >> beam.Map(lambda s: s.decode('utf-8'))
			| "Events data" >> beam.Map(lambda x: {'event_nbr' : x.split(',')[0], 'event_time' : dt.strptime(x.split(',')[1],'%Y-%m-%d %H:%M:%S.%f')})
			| "Event with timestamp" >> beam.Map(lambda events: beam.window.TimestampedValue(events['event_nbr'], events['event_time'].timestamp()))
			| "Event Fixed Window" >> beam.WindowInto(window.FixedWindows(5))
			| "Number of events per window" >> beam.combiners.Count.Globally().without_defaults()
			| "Final results with windowinfo" >> beam.ParDo(AddWindowdtlsFn())
			| "String to BQ row" >> beam.Map(lambda s: {'window_count' : s})
			| "Write to BQ" >> beam.io.WriteToBigQuery(
				table='stream_data',
				dataset='df_streaming_data',
				project='newproject2007',
				schema='window_count:STRING',
				create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
				write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
				)
		)
		
if __name__ == '__main__':
	logging.getLogger().setLevel(logging.INFO)
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--input_topic",
		help="The Cloud Pub/Sub topic to read data from."
		'"projects//topics/".',
		)
	parser.add_argument(
		"--output_path",
		help="GCS file output path including the prefix",
		)
	known_args, pipeline_args = parser.parse_known_args()
	run(
		known_args.input_topic,
		known_args.output_path,
		pipeline_args
		)