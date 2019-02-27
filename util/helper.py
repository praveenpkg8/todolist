from typing import Dict, List


def construct_response_message(**kwargs):
    return kwargs


def Dictnote(**kwargs) -> Dict:
    return kwargs


def Listnote(**kwargs) -> List:
    return kwargs


def extract_sqlalchemy_error(error: str) -> str:
    mes = error.split(')')[1]
    mes = mes.split('(')[1]
    mes = mes.split(',')
    mes = bytes(mes[1], "utf-8").decode("unicode_escape")
    return mes
