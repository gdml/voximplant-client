from collections import OrderedDict
from urllib.parse import parse_qsl, urlparse, urlunparse


def append_to_querytring(url: str, **kwargs) -> str:
    """Append a parameter to the url querystring"""
    url = list(urlparse(url))
    query = OrderedDict(parse_qsl(url[4]))
    query.update(kwargs)

    if not url[2].endswith('/'):  # trailing slash
        url[2] += '/'

    url[4] = '&'.join(f'{p}={v}' for p, v in query.items())

    return urlunparse(url)
