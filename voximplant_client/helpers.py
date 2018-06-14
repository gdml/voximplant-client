from collections import OrderedDict
from urllib.parse import parse_qsl, urlparse, urlunparse


def prepend_slash(input: str) -> str:
    return input if input.startswith('/') else '/' + input


def append_slash(input: str) -> str:
    return input if input.endswith('/') else input + '/'


def remove_trailing_slash(input: str) -> str:
    return input if not input.endswith('/') else input[:-1]


def append_to_querytring(url: str, **kwargs) -> str:
    """Append a parameter to the url querystring"""
    url = list(urlparse(url))
    query = OrderedDict(parse_qsl(url[4]))
    query.update(kwargs)

    url[2] = append_slash(url[2])

    url[4] = '&'.join(f'{p}={v}' for p, v in query.items())

    return urlunparse(url)
