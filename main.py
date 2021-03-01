from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from exceptions import ValidationError
from postback_functions import is_parameter_present_get, is_value_present_get, is_click_id_correct_length_get, \
    is_click_id_numerical_get, is_data_in_body_post, is_parameter_present_post, is_post_parameter_is_one_post, \
    is_value_present_post

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@app.route('/')
def index():
    return 'Ok'


@app.route('/get/', methods=['GET', 'POST'])
@limiter.limit("2 per minute")
def checker():
    if request.method != 'GET':
        return jsonify({"error": "Method Not Allowed",
                        "description": "Use GET"}), 405

    parameters: dict = request.args

    try:
        is_parameter_present_get(parameters)
        is_value_present_get(parameters)
        is_click_id_correct_length_get(parameters)
        is_click_id_numerical_get(parameters)
    except ValidationError as error:
        return jsonify(error.args[0])

    return jsonify({"status": "Success",
                    "description": "Congratulations, GET request was sent correctly"}), 200


@app.route('/post/', methods=['GET', 'POST'])
@limiter.limit("2 per minute")
def checker_post():
    if request.method != 'POST':
        return jsonify({"error": "Method Not Allowed",
                        "description": "Use POST"}), 405

    parameters: dict = request.form

    try:
        is_data_in_body_post(parameters)
        is_parameter_present_post(parameters)
        is_value_present_post(parameters)
        is_post_parameter_is_one_post(parameters)
    except ValidationError as error:
        return jsonify(error.args[0])

    return jsonify({"status": "Success",
                    "description": "Congratulations, POST request was sent correctly"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
