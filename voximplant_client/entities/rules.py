from typing import Optional

from voximplant_client import exceptions, helpers
from voximplant_client.entities.base import BaseVoximplantEntity


class VoxImplantRules(BaseVoximplantEntity):
    def list(self, app_name: str):
        application_id = self.base_client.applications.get_id(app_name)
        if application_id is None:
            raise exceptions.VoxImplantBadApplicationNameException('Non-existant application name given: {}'.format(app_name))

        url = helpers.append_to_querytring('GetRules', application_id=application_id, with_scenarios=True)
        return self.http.get_list(url)

    def get_for_scenario(self, app_name: str, scenario_name: str) -> Optional[dict]:
        raise NotImplemented()
