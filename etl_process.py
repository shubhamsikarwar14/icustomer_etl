import sqlite3
import pandas as pd


def ingest_data(file_path):
    """
    Ingests data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: The ingested data as a pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """
    Cleans the ingested data by handling missing values and ensuring correct data types.

    Parameters:
    df (DataFrame): The ingested data.

    Returns:
    DataFrame: The cleaned data.
    """
    df.fillna({
        'interaction_id': 'unknown',
        'user_id': 'unknown',
        'product_id': 'unknown',
        'action': 'unknown',
        'timestamp': pd.Timestamp.now()
    }, inplace=True)

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    return df


def transform_data(df):
    """
    Transforms the data by calculating interaction counts per user and product.

    Parameters:
    df (DataFrame): The cleaned data.

    Returns:
    DataFrame: The transformed data with interaction counts.
    """
    interaction_counts = df.groupby(
        ['user_id', 'product_id']).size().reset_index(name='interaction_count')
    df = df.merge(interaction_counts, on=['user_id', 'product_id'], how='left')

    return df


def load_data_to_sqlite(df, db_name='db/interactions.db'):
    """
    Loads the transformed data into a SQLite database.

    Parameters:
    df (DataFrame): The transformed data.
    db_name (str): The name of the SQLite database file.
    """
    conn = sqlite3.connect(db_name)
    df.to_sql('user_interactions', conn, if_exists='replace', index=False)
    conn.close()


def main():
    """
    Main function to perform the ETL process.
    """
    file_path = '{REPLACE_WITH_ABSOLUTE_PATH}/data/input/example_interactions.csv'  # Replace with the actual path to your CSV file
    df = ingest_data(file_path)
    df = clean_data(df)
    df = transform_data(df)
    load_data_to_sqlite(df)


if __name__ == "__main__":
    main()
