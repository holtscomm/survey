"""
__init__.py
"""


def list_get_or_default(list_to_get, index, default=None):
    try:
        return list_to_get[index]
    except IndexError:
        return default
