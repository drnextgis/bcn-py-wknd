from flask import Flask, render_template, jsonify, request
from dateutil.parser import parse as date_parse

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["get"])
def search():
    # searchForm: {
    #     departure: new Date(2019, 9, 16),
    #     return: new Date(2096, 9, 16),
    #     from: '',
    #     to: ''
    # }
    searchForm = request.args

    parsedSearchForm = {
        "from": searchForm["from"],
        "to": searchForm["to"],
        "from_date": date_parse(searchForm["departure"]),
        "to_date": date_parse(searchForm["return"]),
    }

    search_results = [
        {
            "from": "BCN",
            "to": "PRG",
            "departure": "2019, 9, 16",
            "return": "2096, 9, 16",
            "price": 200.5,
        },
        {
            "from": "BCN",
            "to": "PRG",
            "departure": "2019, 9, 17",
            "return": "2096, 9, 18",
            "price": 200.5,
        },
    ]
    return jsonify(results=search_results)


if __name__ == "__main__":
    app.run(port=8080)
