import json
from functools import wraps
from flask import request
from modules.registration.parser import Parser
from status import Status
from util.exceptions import EmailFormatException, MobileNumberFormatException
from util.helper import construct_response_message


def verify_signup_reququest(fn):

    @wraps(fn)
    def decorated_function(*args, **kwargs):
        request_data = request.get_json()

        fields = ['first_name', 'username', 'email', 'dob', 'mobile_number',
                  'address_1', 'state', 'country', 'pin_code', 'college',
                  'department', 'year']

        for key in fields:

            if key not in list(request_data.key()):
                pass

            if key not in request_data.key() or request_data[key] == "" or request_data is None:
                pass

            if key == fields[3]:
                try:
                    Parser.parse_email(request_data['email'])
                except EmailFormatException as e:
                    message = construct_response_message(error_message=e.error_message)
                    return json.dumps(message), Status.HTTP_400_BAD_REQUEST


            if key == fields[5]:
                try:
                    Parser.parse_mobile_number(request_data['mobile_number'])
                except MobileNumberFormatException as e:
                    message = construct_response_message(error_message=e.error_message)
                    return  json.dumps(message), Status.HTTP_400_BAD_REQUEST
                pass
        pass

    return decorated_function
