from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime as dtime

# Define the default arguments for the DAG
def_args = {
    "owner": "airflow",
    "start_date": dtime(2024, 9, 29),
}

# Define a simple function for each task
def start_task():
    print("Starting the ETL process.")

def extract_task():
    print("Extracting data.")

def transform_task():
    print("Transforming data.")

def load_task():
    print("Loading data.")

def end_task():
    print("ETL process finished.")

# Create the DAG
with DAG("ETL",
         catchup=False,
         default_args=def_args,
         schedule_interval='@daily'  # Adjust as needed
         ) as dag:
    
    start = PythonOperator(
        task_id="START",
        python_callable=start_task
    )
    
    extract = PythonOperator(
        task_id="Extract",
        python_callable=extract_task
    )
    
    transform = PythonOperator(
        task_id="Transform",
        python_callable=transform_task
    )
    
    load = PythonOperator(
        task_id="Load",
        python_callable=load_task
    )
    
    end = PythonOperator(
        task_id="END",
        python_callable=end_task
    )
    
    # Set task dependencies
    start >> extract >> transform >> load >> end
