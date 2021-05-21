import json
from typing import List

from flask import Flask, request

app = Flask(__name__)


@app.route("/shifted_array/", methods=["POST"])
def _shifted_array():
    form_data = request.get_data(as_text=True)

    shifted_array: List[int] = json.loads(form_data)

    low = 0
    high = len(shifted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        if low == high:
            return f"{shifted_array[low - 1]}"
        if shifted_array[0] < shifted_array[mid] < shifted_array[high]:
            return f"{shifted_array[0]}"
        if shifted_array[mid - 1] > shifted_array[mid] and shifted_array[mid] < shifted_array[mid + 1]:
            return f"{shifted_array[mid - 1]}"
        else:
            if shifted_array[mid] > shifted_array[high]:
                low = mid + 1
            else:
                high = mid - 1

    return "-1"


if __name__ == "__main__":
    app.run(debug=True)
