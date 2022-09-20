from typing import Union


def reverse_string(string: str) -> Union[str, int]:
    if not string:
        return -1
    if not len(string.strip()):
        return -2
    return ''.join(reversed(string))
