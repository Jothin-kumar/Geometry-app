dictionary = {}


def set_value(key: str, value):
    dictionary[key] = value


def get_value(key: str):
    try:
        return dictionary[key]
    except KeyError:
        return []
