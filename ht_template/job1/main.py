"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""
from flask import Flask, request


import api
import storage

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    auth_token = request.headers['Authorization']
    data = request.headers['data']
    raw_dir = request.headers['raw_dir']

    if not auth_token:
        print("AUTH_TOKEN environment variable must be set")

    sales = api.get_sales(data, auth_token)
    storage.save_to_disk(sales, raw_dir)
    return {
               'sales': api.get_sales(data, auth_token)

           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8081)
