from flask import Flask

app = Flask(__name__)


def sum_of_range(range_size):
    high_index = range_size - 1
    return (high_index * range_size) >> 1


@app.route('/total')
def total_value():
    range_size = 10000001
    response = {
        "total": sum_of_range(range_size)
    }
    return response


