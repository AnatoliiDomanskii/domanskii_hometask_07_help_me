from flask import Flask, request
from fastavro import parse_schema, writer
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():

    raw_dir = request.json.get('raw_dir')
    stg_dir = request.json.get('stg_dir')

    print(raw_dir)
    print(stg_dir)

    schema = {
        'name': 'Sales',
        'type': 'record',
        'fields': [
            {'name': 'client', 'type': 'string'},
            {'name': 'purchase_date', 'type': 'string'},
            {'name': 'product', 'type': 'string'},
            {'name': 'price', 'type': 'int'}
        ],
    }
    parsed_schema = parse_schema(schema)

    with open(raw_dir + '.json', 'r') as file_in:
        records = json.load(file_in)
        with open(stg_dir + '.avro', 'wb') as out:
            writer(out, parsed_schema, records)

    return {
               "message": "Data retrieved successfully from API"
    }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)
