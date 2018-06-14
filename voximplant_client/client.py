
from voximplant_client.entities.applications import VoxImplantApplications
from voximplant_client.entities.rules import VoxImplantRules
from voximplant_client.entities.scenarios import VoxImplantScenarios
from voximplant_client.http import VoximplantHTTPClient


class VoximplantClient:
    def __init__(
        self,
        account_id: str,
        api_key: str,
        host: str='https://api.voximplant.com/platform_api',
    ):
        self.http = VoximplantHTTPClient(account_id, api_key, host)

        self.applications = VoxImplantApplications(self)
        self.rules = VoxImplantRules(self)
        self.scenarios = VoxImplantScenarios(self)
