# Data Engineering Coding Test

# TASK 1- Data Ingestion and ETL

1. Ensure you have the required dependencies installed:
    ```sh
    pip install pandas
    pip install sqlite3
    ```

2. Save the CSV input as `example_interactions.csv` in the same directory as the script.

3. Run the ETL process script to generate the SQLite database file:
    ```sh
    python etl_process.py
    ```

4. The cleaned and transformed data will be loaded into a SQLite database named `interactions.db`.

### File Structure

|-- data
| |-- input
| | |--  example_interactions.csv
| |-- output
|-- db
| |-- interactions.db
|-- etl_process.py
|-- README.md

### Note
Make sure to replace 'example_interactions.csv' with the actual path to your CSV file in the script if necessary. The script will handle data ingestion, cleaning, transformation, and loading into the SQLite database.


# Task 2- To automate the ETL process using Apache Airflow.

### Prerequisites

1. Install Apache Airflow by following the official [Airflow installation guide](https://airflow.apache.org/docs/apache-airflow/stable/start.html).

2. Ensure you have the required dependencies installed:
    ```sh
    pip install pandas
    pip install sqlite3
    ```

### Setting Up Airflow

1. Set up the Airflow home directory:
    ```sh
    export AIRFLOW_HOME=~/airflow
    ```

2. Initialize the Airflow database:
    ```sh
    airflow db init
    ```

3. Create an Airflow user:
    ```sh
    airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com
    ```

4. Start the Airflow web server:
    ```sh
    airflow webserver --port 8080
    ```

5. Start the Airflow scheduler:
    ```sh
    airflow scheduler
    ```

### Creating the DAG

1. Save the `dag_etl_pipeline_dag.py` script in the `dags` directory of your Airflow home (e.g., `~/airflow/dags/dag_etl_pipeline.py`).

2. Save the example CSV input as `example_interactions.csv` in the directory mentioned in your dag.

### Running the DAG

1. Open the Airflow web UI by navigating to `http://localhost:8080` in your web browser.

2. Activate the DAG named `etl_pipeline`.

3. Trigger the DAG manually to run it immediately or wait for it to run based on the defined schedule (daily).

### Error Handling

- The DAG includes basic error handling and logging within each task to manage and record any issues that occur during the ETL process.

### File Structure

|-- dags
| |-- dag_etl_pipeline.py


### Note
Make sure to replace 'example_interactions.csv' with the actual path to your CSV file in the script if necessary. The DAG will handle data ingestion, cleaning, transformation, and loading into the SQLite database.

# Task 3- To implement a solution to store and retrieve user interaction data efficiently.

### Schema Creation and Data Insertion

1. Ensure you have a PostgreSQL database set up. You can use the following command to create a new database:
    ```sh
    createdb interactions_db
    ```

2. Connect to the database:
    ```sh
    psql interactions_db
    ```

3. Execute the schema creation and data insertion script:
    ```sh
    \i schema_and_data_insertion.sql
    ```

### Data Retrieval

1. Execute the data retrieval queries to get the required information:
    ```sh
    \i data_retrieval_queries.sql
    ```

### Optimization Techniques

Refer to the `optimization_techniques.md` document for detailed information on optimization techniques used to improve the performance of the data retrieval queries.

### Final File Structure

|-- dags
| |-- dag_etl_pipeline.py
|-- data
| |-- input
| | |--  example_interactions.csv
| |-- output
|-- db
| |-- data_retrieval_queries.sql
| |-- interactions.db
| |-- schema_and_data_insertion.sql
|-- etl_process.py
|-- optimization_techniques.md
|-- README.md