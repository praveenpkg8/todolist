from flask import (Flask, Blueprint, request)
from modules.registration.composed import verify_signup_reququest

registration_bp = Blueprint('registration', __name__, url_prefix='/registration')


@registration_bp.route('/create', methods=["PUT"])
@verify_signup_reququest
def sign_up_form():



    pass
