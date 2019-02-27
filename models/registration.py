import datetime
from typing import Tuple, Dict
import logging

from sqlalchemy.exc import IntegrityError

from models import db

logger = logging.getLogger(__name__)

class UserCredentials(db.Model):

    __tablename__ = "user_details"

    id = db.Column(db.String(128), unique=True, primary_key=True)
    first_name = db.Column(db.String(24))
    last_name = db.Column(db.String(24))
    username = db.Column(db.String(24), unique=True)
    email = db.Column(db.String(48), unique=True)
    dob = db.Column(db.DateTime())
    mobile_number = db.Column(db.String(10), unique=True)
    address_1 = db.Column(db.String(128))
    address_2 = db.Column(db.String(128))
    city = db.Column(db.String(128))
    state = db.Column(db.String(128))
    country = db.Column(db.String(128))
    pin_code = db.Column(db.String(7))
    college = db.Column(db.String(128))
    department = db.Column(db.String(128))
    year = db.Column(db.Integer)


    def __init__(self, first_name, last_name, username,
                 email, dob, mobile_number, address_1,
                 address_2, city, state, country, pin_code,
                 college, department, year):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.dob = dob
        self.mobile_number = mobile_number
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.country = country
        self.pin_code = pin_code
        self.college = college
        self.department = department
        self.year = year

    def create_new_account(self) -> Tuple['bool', Dict]:
        try:
            db.session.add(self)
            db.session.commit()

        except IntegrityError as e:
            db.session.rollback()
            from util.helper import extract_sqlalchemy_error
            message: str = f"Account: {extract_sqlalchemy_error(error=e.message())}"
            logger.error(message)
            message_dict: Dict[str, str] = {
                "message": message
            }
            return False, message_dict

        message_dict: Dict[str, str] = {
            "message": "Successfully added record"
        }
        return True, message_dict

