from datetime import datetime, timedelta
import sqlite3
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd


def ingest_data(**kwargs):
    """
    Ingests data from a CSV file and saves it to an intermediate file.

    Parameters:
    kwargs (dict): Keyword arguments containing context and other information.
    """
    file_path = kwargs.get(
        'file_path', '{REPLACE_WITH_ABSOLUTE_PATH}/example_interactions.csv')
    df = pd.read_csv(file_path)
    df.to_csv('/tmp/raw_data.csv', index=False)


def clean_data(**kwargs):
    """
    Cleans the ingested data by handling missing values and ensuring correct data types.
    Saves the cleaned data to an intermediate file.

    Parameters:
    kwargs (dict): Keyword arguments containing context and other information.
    """
    df = pd.read_csv('/tmp/raw_data.csv')
    df.fillna({
        'interaction_id': 'unknown',
        'user_id': 'unknown',
        'product_id': 'unknown',
        'action': 'unknown',
        'timestamp': pd.Timestamp.now()
    }, inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.to_csv('/tmp/cleaned_data.csv', index=False)


def transform_data(**kwargs):
    """
    Transforms the data by calculating interaction counts per user and product.
    Saves the transformed data to an intermediate file.

    Parameters:
    kwargs (dict): Keyword arguments containing context and other information.
    """
    df = pd.read_csv('/tmp/cleaned_data.csv')
    interaction_counts = df.groupby(
        ['user_id', 'product_id']).size().reset_index(name='interaction_count')
    df = df.merge(interaction_counts, on=['user_id', 'product_id'], how='left')
    df.to_csv('/tmp/transformed_data.csv', index=False)


def load_data_to_sqlite(**kwargs):
    """
    Loads the transformed data into a SQLite database.

    Parameters:
    kwargs (dict): Keyword arguments containing context and other information.
    """
    df = pd.read_csv('/tmp/transformed_data.csv')
    conn = sqlite3.connect('interactions.db')
    df.to_sql('user_interactions', conn, if_exists='replace', index=False)
    conn.close()


# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='An ETL pipeline',
    schedule_interval=timedelta(days=1),
)

# Define the tasks
ingest_data_task = PythonOperator(
    task_id='ingest_data',
    python_callable=ingest_data,
    provide_context=True,
    dag=dag,
)

clean_data_task = PythonOperator(
    task_id='clean_data',
    python_callable=clean_data,
    provide_context=True,
    dag=dag,
)

transform_data_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    provide_context=True,
    dag=dag,
)

load_data_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data_to_sqlite,
    provide_context=True,
    dag=dag,
)

# Set task dependencies
ingest_data_task >> clean_data_task >> transform_data_task >> load_data_task
