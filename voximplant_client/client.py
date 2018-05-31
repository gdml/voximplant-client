import requests


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
