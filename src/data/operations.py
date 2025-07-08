import os
import pandas as pd
from azure.storage.blob import BlobServiceClient
import io
from dotenv import load_dotenv
import requests
from pymongo import MongoClient
from sqlalchemy import create_engine, text, MetaData, Table, select
import psycopg2


load_dotenv()


def read_local_file_csv(filepath):
    csv_data = pd.read_csv(filepath)
    return csv_data


def read_blob_file(container_name, blob_name):
    connection_string = os.getenv("AZURE_BLOB_CONNECTION")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=blob_name
    )

    stream = blob_client.download_blob().readall()
    result = pd.read_csv(io.BytesIO(stream))
    return result


def fetch_api_data(url):
    response = requests.get(url)
    response.raise_for_status()
    results = response.json()
    return results


def connect_to_mongo():
    connection_string = os.getenv("FULL_MONGO_DB_CONNECTION")
    client = MongoClient(connection_string)
    return client


def insert_data_to_mongo(client, database_name, collection_name, data):
    db = client.get_database(database_name)
    collection = db[collection_name]
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)
    print("Data inserted successfully.")


def query_and_verify_mongo_data(client, database_name, collection_name):
    db = client.get_database(database_name)
    collection = db[collection_name]
    single_user = collection.find_one()
    print(f"Sample user data: {single_user}")


def connect_to_postgres():
    connection_string = os.getenv("POSTGRES_DB_CONNECTION")
    engine = create_engine(connection_string)
    connection = engine.connect()
    return connection


def call_stored_proc_or_function():
    # callproc method for functions
    # execute for called procs
    proc_name1 = "get_team_captains"
    function_name1 = "get_team_captains_function"
    conn = None
    try:
        conn = psycopg2.connect(os.getenv("POSTGRES_DB_CONNECTION"))
        cursor = conn.cursor()

        # function
        cursor.callproc(function_name1)
        results = cursor.fetchall()
        for row in results:
            print(row)

        # stored procedure
        cursor.execute(f"CALL {proc_name1}()")

    except Exception as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
