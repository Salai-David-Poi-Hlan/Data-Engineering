import datetime as dt
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd

def CSVToJson():
    # Corrected file path and CSV reading
    df = pd.read_csv('data.CSV')  # use read_csv, not read_CSV
    for i, r in df.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.json', orient='records')  # use to_json, not to_JSON

default_args = {
    'owner': 'paulcrickard',
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('MyCSVDAG',
         default_args=default_args,
         schedule_interval='0 * * * *',
         catchup=False) as dag:  # Added catchup for clarity

    print_starting = BashOperator(
        task_id='starting',
        bash_command='echo "I am reading the CSV now....."'
    )

    CSVJson = PythonOperator(
        task_id='convertCSVtoJson',
        python_callable=CSVToJson
    )

    print_starting >> CSVJson  # Simplified task dependency setting

