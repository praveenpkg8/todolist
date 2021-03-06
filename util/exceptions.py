class NoteNotFoundException(Exception):

    def __init__(self, value):
        self.error_message = value


class RecordNotFoundException(Exception):

    def __init__(self, value):
        self.error_message = value


class DataBaseSessionException(Exception):

    def __init__(self, value):
        self.error_message = value


class NoteDeletedException(Exception):

    def __init__(self, value):
        self.error_message = value


class EmailFormatException(Exception):

    def __init__(self, value):
        self.error_message = value


class MobileNumberFormatException(Exception):

    def __init__(self, value):
        self.error_message = value


class MobileNumberLengthException(Exception):

    def __init__(self, value):
        self.error_message = value
