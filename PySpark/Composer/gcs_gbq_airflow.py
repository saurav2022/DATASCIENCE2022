from airflow import models
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocSubmitJobOperator,
    DataprocDeleteClusterOperator,
)
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
    GCSToBigQueryOperator,
)

CLUSTER_NAME = "dataproc-airflow-cluster"
REGION = "us-central1"
PROJECT_ID = "gcp11oct"
GCS_GCS_PYSPARK_URI = "gs://dp-airflow-bkt/Code/gcs_gcs.py"
BQ_BQ_PYSPARK_URI = "gs://dp-airflow-bkt/Code/bq_bq.py"
GCS_BUCKET = "dp-airflow-bkt"
BQ_TABLE = "gcp11oct.ds_hmda.gcs_parquet_to_bq"

CLUSTER_CONFIG = {
    "master_config": {
        "num_instances": 1,
        "machine_type_uri": "n2-standard-2",
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 50},
    },
    "worker_config": {
        "num_instances": 2,
        "machine_type_uri": "n2-standard-2",
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 50},
    },
    "software_config": {
        "image_version": "2.1-debian11",
        "optional_components": ["JUPYTER"],
    },
}

GCS_GCS_PYSPARK_JOB = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": {"main_python_file_uri": GCS_GCS_PYSPARK_URI},
}

BQ_BQ_PYSPARK_JOB = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": {"main_python_file_uri": BQ_BQ_PYSPARK_URI},
}

with models.DAG(
    "dataproc_airflow_gcs_to_gbq_v4",
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    tags=["dataproc_airflow"],
) as dag:
    create_cluster = DataprocCreateClusterOperator(
        task_id="create-cluster",
        project_id=PROJECT_ID,
        cluster_config=CLUSTER_CONFIG,
        region=REGION,
        cluster_name=CLUSTER_NAME,
    )

    gcs_gcs_job = DataprocSubmitJobOperator(
        task_id="GCS_GCS_Transfer",
        job=GCS_GCS_PYSPARK_JOB,
        region=REGION,
        project_id=PROJECT_ID,
    )

    gcs_to_gbq = GCSToBigQueryOperator(
        task_id="GCS_BQ_Transfer",
        bucket=GCS_BUCKET,
        source_objects=["output_files/*.snappy.parquet"],
        destination_project_dataset_table=BQ_TABLE,
        source_format="PARQUET",
        write_disposition="WRITE_APPEND",
    )

    delete_cluster = DataprocDeleteClusterOperator(
        task_id="delete_cluster",
        project_id=PROJECT_ID,
        cluster_name=CLUSTER_NAME,
        region=REGION,
    )

    bq_to_bq_job = DataprocSubmitJobOperator(
        task_id="BQ_BQ_Transfer",
        job=BQ_BQ_PYSPARK_JOB,
        region=REGION,
        project_id=PROJECT_ID,
    )
    create_cluster >> gcs_gcs_job >> gcs_to_gbq >> bq_to_bq_job >> delete_cluster
