import apache_beam as beam

with beam.Pipeline() as pipeline:
	total_elements = (
		pipeline
		| 'Create fruits' >> beam.Create(
			[('mango', 'Malda'), 
			 ('apple', 'Kashmiri'), 
			 ('avocado','A'), 
			 ('papaya', 'P'), 
			 ('mango', 'Ratnagiri'), 
			 ('pineapple', 'P'), 
			 ('guava', 'G'), 
			 ('banana', 'Hyderabad'), 
			 ('avocado','A'), 
			 ('strawberry', 'S'), 
			 ('banana', 'Nasik')]
			)
		| 'Count all elements' >> beam.combiners.Count.PerKey()
		| beam.Map(print)
		)

if __name__ == '__main__':
	print("Frequency of elements are displayed here.")