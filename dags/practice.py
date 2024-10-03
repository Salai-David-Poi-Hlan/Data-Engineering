from airflow import DAG
from airflow.utils.dates import days_ago 
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd

def CSVtoJson():
    df = pd.read_csv("data.CSV")
    for i, r in df.iterrows():  # Added parentheses to iterrows()
        print(r['name'])
    df[['name']].to_json("fromAirFlow.json", orient="records")  # Save only the 'name' column

dag = DAG(
    "CSVtoJSON",
    default_args={"start_date": days_ago(1)},
    catchup=False,
    schedule_interval="0 19 * * *"
)

print_starting = BashOperator(
    task_id="Start",
    bash_command='echo "I am reading the CSV now...."',
    dag=dag
)

CSV_JSON = PythonOperator(
    task_id="CSVtoJSON",
    python_callable=CSVtoJson,
    dag=dag
)

print_starting >> CSV_JSON
CSVtoJson()