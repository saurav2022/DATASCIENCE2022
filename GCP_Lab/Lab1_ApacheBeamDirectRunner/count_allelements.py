import apache_beam as beam

with beam.Pipeline() as pipeline:
	total_elements = (
		pipeline
		| 'Create fruits' >> beam.Create(
			['mango', 'apple', 'avocado', 'papaya', 'mango', 'pineapple', 'guava', 'banana', 'avocado', 'strawberry', 'banana']
			)
		| 'Count all elements' >> beam.combiners.Count.Globally()
		| beam.Map(print)
		)

if __name__ == '__main__':
	print("Frequency of elements are displayed here.")