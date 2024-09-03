from pyspark.sql import SparkSession
from pyspark.sql.functions import *

GCS_DATA_SOURCE_PATH = "gs://dp-airflow-bkt1/data/hmda.csv"
GCS_DATA_OUTPUT_PATH = "gs://dp-airflow-bkt1/output_files/"


def gcs_gcs_run():
    spark = SparkSession.builder.appName("my_gcp_app").getOrCreate()
    data = spark.read.csv(GCS_DATA_SOURCE_PATH, header=True)
    subset_data = data.select(
        "loan_purpose_name",
        "county_name",
        "county_code",
        "applicant_ethnicity",
        "applicant_sex_name",
        "applicant_income_000s",
    )
    subset_data.write.mode("overwrite").parquet(GCS_DATA_OUTPUT_PATH)
    print(f"GCS to GCS transfer successful. Total number of records : {data.count()}")


if __name__ == "__main__":
    gcs_gcs_run()
