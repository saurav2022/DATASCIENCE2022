from google.cloud import pubsub_v1
import time
import datetime as dt 

project_id = 'newproject2007'
topic_id = 'pubsub_df_demo'

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

for event_nbr in range(1, 100):
	data_str = f'{event_nbr},{dt.datetime.now()}'
	data = data_str.encode('utf-8')
	time.sleep(1)
	future=publisher.publish(topic_path, data, origin="python-sample", username='gcp')
	print(data)

print(f"Published messages with custom attributes to {topic_path}")