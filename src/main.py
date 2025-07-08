from data.operations import (
    read_blob_file,
    read_local_file_csv,
    fetch_api_data,
    connect_to_mongo,
    insert_data_to_mongo,
    query_and_verify_mongo_data,
)


def main():
    # READING LOCAL DATA
    # sample_customers = "../data/sample_customers.csv"
    # local_sample = read_local_file_csv(sample_customers).head()
    # print("reading local file", local_sample)

    # READING CLOUD DATA (AZURE)
    # container = "customers"
    # blob_name = "sample_customers.csv"
    # blob_sample = read_blob_file(container, blob_name).head()
    # print("reading blob file", blob_sample)

    # READING API DATA
    # api_url = "https://jsonplaceholder.typicode.com/users"
    # api_data = fetch_api_data(api_url)

    # READ/WRITE MONGO DATA
    # mongo_target_database = "Cluster0"
    # mongo_target_collection = "module_2_skills_check"
    # mongo_client = connect_to_mongo()
    # insert_data_to_mongo(
    #     mongo_client, mongo_target_database, mongo_target_collection, api_data
    # )

    # query_and_verify_mongo_data(
    #     mongo_client, mongo_target_database, mongo_target_collection
    # )

    # READING POSTGRES DATA
    pass


if __name__ == "__main__":
    main()
