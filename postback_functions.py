from exceptions import ValidationError


def is_parameter_present_get(parameters: dict):
    mandatory_keys = ['click_id', 'order_id', 'sub_id']
    for key in mandatory_keys:
        if key not in parameters.keys():
            raise ValidationError({"error": f"{key} not present",
                                   "description": f"add the {key}"})


def is_value_present_get(parameters: dict):
    for key, value in parameters.items():
        if value == '':
            raise ValidationError({"error": f"{key} is empty",
                                   "description": f"fill the {key}"})


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
