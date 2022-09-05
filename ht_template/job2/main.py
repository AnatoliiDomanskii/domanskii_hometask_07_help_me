from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    return "111"


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)
