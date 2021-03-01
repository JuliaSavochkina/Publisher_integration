from exceptions import ValidationError


def is_parameter_present_get(parameters: dict):
    mandatory_keys: list = ['click_id', 'order_id', 'sub_id']
    for key in mandatory_keys:
        if key not in parameters.keys():
            raise ValidationError({"error": f"parameter '{key}' not present",
                                   "description": f"add the '{key}' parameter"})


def is_value_present_get(parameters: dict):
    for key, value in parameters.items():
        if value == '':
            raise ValidationError({"error": f"parameter '{key}' is empty",
                                   "description": f"fill the '{key}' value"})


def is_click_id_correct_length_get(parameters: dict):
    for key, value in parameters.items():
        if key == 'click_id' and len(str(value)) != 10:
            raise ValidationError({"error": "wrong click_id",
                                   "description": "click_id length should be 10 symbols"})


def is_click_id_numerical_get(parameters: dict):
    for key, value in parameters.items():
        if key == 'click_id' and not value.isdigit():
            raise ValidationError({"error": "wrong click_id",
                                   "description": "click_id should be numerical"})


def is_data_in_body_post(parameters: dict):
    if not parameters:
        raise ValidationError({"error": "wrong data type",
                               "description": "data should be passed only in body"})


def is_parameter_present_post(parameters: dict):
    mandatory_keys: list = ['click_id', 'order_id', 'sub_id', 'post']
    for key in mandatory_keys:
        if key not in parameters.keys():
            raise ValidationError({"error": f"parameter '{key}' not present",
                                   "description": f"add the '{key}' parameter"})


def is_value_present_post(parameters: dict):
    for key, value in parameters.items():
        if value == '':
            raise ValidationError({"error": f"parameter '{key}' is empty",
                                   "description": f"fill the '{key}' value"})


def is_post_parameter_is_one_post(parameters: dict):
    for key, value in parameters.items():
        if key == 'post' and value != '1':
            raise ValidationError({"error": "wrong value of 'post'",
                                   "description": "'post' must be equal to 1"})
