from typing import Optional

from voximplant_client import exceptions, helpers
from voximplant_client.entities.base import BaseVoximplantEntity


class VoxImplantRules(BaseVoximplantEntity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._rule_cache = dict()

    def _get_application_id(self, app) -> int:
        application_id = self.base_client.applications.get_id(app)
        if application_id is None:
            raise exceptions.VoxImplantBadApplicationNameException('Non-existant application name given: {}'.format(app))

        return application_id

    def list(self, app: str):
        application_id = self._get_application_id(app)
        url = helpers.append_to_querytring('GetRules', application_id=application_id, with_scenarios=True)
        return self.http.get_list(url)

    def add(self, app: str, name: str, scenario: str, rule_pattern: str = '.*'):
        """Add a new scenario"""
        return self.http.post('AddRule', payload=dict(
            application_id=self._get_application_id(app),
            rule_name=name,
            scenario_name=scenario,
            rule_pattern=rule_pattern,
        ))

    def _get_cached_rules_list(self, app: str):
        if app not in self._rule_cache:
            self._rule_cache[app] = self.list(app)

        return self._rule_cache[app]

    def get_for_scenario(self, app: str, scenario: str) -> Optional[int]:
        for rule in self._get_cached_rules_list(app).result:
            for rule_scenario in rule.get('scenarios', []):
                if rule_scenario['scenario_name'] == scenario:
                    return rule['rule_id']
