import re

from util.exceptions import EmailFormatException, MobileNumberFormatException, MobileNumberLengthException

EMAIL_REGEX = "\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
MOBILE_REGEX = '^[6-9]\d{9}$'


class Parser:

    @staticmethod
    def parse_email(mail: str) -> bool:
        is_valid = re.search(pattern=EMAIL_REGEX, string=mail)
        if not is_valid:
            raise EmailFormatException("Invalid Email id Format")
        return True

    @staticmethod
    def parse_mobile_number(mobile_number: str) -> bool:
        if len(mobile_number) != 10:
            raise MobileNumberLengthException("Invalid Mobile Number Length")

        is_valid = re.search(pattern=MOBILE_REGEX, string=mobile_number)
        if not is_valid:
            raise MobileNumberFormatException("Invalid Mobile Number Format")

        return True
