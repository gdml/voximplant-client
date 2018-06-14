from urllib.parse import urljoin

import requests

from voximplant_client import helpers


class VoximplantClient:

    def __init__(
        self,
        account_id: str,
        api_key: str,
        host: str='https://api.voximplant.com',
    ):
        self.host = host
        self.account_id = account_id
        self.api_key = api_key

    def format_url(self, url: str) -> str:
        print(self.host)
        url = urljoin(self.host, url)
        return helpers.append_to_querytring(
            url,
            account_id=self.account_id,
            api_key=self.api_key,
        )
