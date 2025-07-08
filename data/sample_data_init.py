import pandas as pd
import json


def create_initial_data():
    customers_data = {
        "customer_id": range(1, 101),
        "name": (["John Smith", "Jane Doe", "Bob Johnson"] * 33) + ["John Smith"],
        "email": (["john@email.com", "jane@email.com", "bob@email.com"] * 33)
        + ["john@email.com"],
        "order_amount": ([100.50, 200.75, 150.00] * 33) + [100.50],
    }
    pd.DataFrame(customers_data).to_csv("sample_customers.csv", index=False)

    # Sample JSON data
    with open("sample_config.json", "w") as f:
        json.dump(
            {"api_url": "https://jsonplaceholder.typicode.com&#39", "timeout": 10}, f
        )


create_initial_data()
