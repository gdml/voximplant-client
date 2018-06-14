from collections import OrderedDict
from typing import Iterable

import requests

from voximplant_client import helpers


class VoxImplantAPIResult(OrderedDict):
    @property
    def result(self) -> Iterable:
        return self.get('result', [])


class VoxImplantClientException(BaseException):
    pass


class VoximplantClient:
    def __init__(
        self,
        account_id: str,
        api_key: str,
        host: str='https://api.voximplant.com/platform_api',
    ):
        self.host = helpers.remove_trailing_slash(host)
        self.account_id = account_id
        self.api_key = api_key

    def format_url(self, url: str) -> str:
        url = helpers.prepend_slash(url)
        url = self.host + url

        return helpers.append_to_querytring(
            url,
            account_id=self.account_id,
            api_key=self.api_key,
        )
