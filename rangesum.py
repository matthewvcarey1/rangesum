from flask import Flask

app = Flask(__name__)


def sum_of_range(num_range):
    range_size = len(num_range)
    high_index = range_size - 1
    n1 = num_range[0]
    n2 = num_range[high_index]
    return (range_size * (n1 + n2)) >> 1


@app.route('/total')
def total_value():
    num_range = range(10000001)
    response = {
        "total": sum_of_range(num_range)
    }
    return response
