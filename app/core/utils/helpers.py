from datetime import datetime


def datetime_to_string(value, format='%Y-%m-%d %H:%M:%S'):
    """
    Transforma datetime em string no formato %Y-%m-%d %H:%M:%S.
    """
    return value.strftime(format)


def string_to_datetime(string, format='%Y-%m-%d %H:%M:%S'):
    """
    Transforma uma string em datetime.
    """
    return datetime.strptime(string, format)
