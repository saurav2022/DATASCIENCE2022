from pyspark.sql import SparkSession

BQ_SRC_TABLE = "gcp11oct.ds_hmda.gcs_parquet_to_bq"
BQ_DEST_TABLE = "gcp11oct.ds_hmda.county_distribution"

spark = SparkSession.builder.master("yarn").appName("bq_to_bq_transform").getOrCreate()

BUCKET = "dp-airflow-bkt"
spark.conf.set("temporaryGcsBucket", BUCKET)

hmda = spark.read.format("bigquery").option("table", BQ_SRC_TABLE).load()

hmda.createOrReplaceTempView("hmda")

county_count = spark.sql(
    "SELECT county_name, count(1)  FROM hmda     group by county_name order by 2 desc LIMIT 20"
)
county_count.show()
county_count.printSchema()

county_count.write.format("bigquery").option("table", BQ_DEST_TABLE).mode(
    "append"
).save()
