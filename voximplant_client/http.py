import requests

from voximplant_client import exceptions, helpers
from voximplant_client.result import VoxImplantAPIResult


class VoximplantHTTPClient:
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

    def get(self, url: str) -> VoxImplantAPIResult:
        response = requests.get(self.format_url(url))
        if response.status_code != 200:
            raise exceptions.VoxImplantClientException('Non-200 returned for {}: {}'.format(url, response.status_code))

        return VoxImplantAPIResult(response.json())
