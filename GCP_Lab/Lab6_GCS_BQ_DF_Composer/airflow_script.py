from airflow import models
from airflow import DAG
import airflow
from datetime import datetime, timedelta
from airflow.contrib.operators.dataflow_operator import DataFlowPythonOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    "owner": "Airflow",
    "retries": 1,
    "retry_delay": timedelta(seconds=50),
    "dataflow_default_options": {
        "project": "newproject2007",
        "region": "us-central1",
        "runner": "DataflowRunner",
    },
}

dag = DAG(
    dag_id="Titanic_Survived",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=airflow.utils.dates.days_ago(1),
    catchup=False,
    description="DAG for data ingestion and transformation.",
)

start = DummyOperator(task_id="start_task_id", dag=dag)

dataflow_task = DataFlowPythonOperator(
    task_id="python_task_dataflow",
    py_file="gs://databkt2024/scripts/dataflow_script_tiranic.py",
    options={"input": "gs://databkt2024/titanic_dataset.csv"},
    dag=dag,
)

end = DummyOperator(task_id="end_task_id", dag=dag)

start >> dataflow_task >> end
