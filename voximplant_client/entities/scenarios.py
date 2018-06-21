from voximplant_client.entities.base import BaseVoximplantEntity


class VoximplantScenarios(BaseVoximplantEntity):
    list_endpoint = 'GetScenarios'

    def add(self, name: str, file: str):
        with open(file, 'r') as f:
            script = f.read()  # maybe add some preprocessing later

        return self.http.post('AddScenario', dict(
            scenario_name=name,
            scenario_script=script,
            rewrite=True,
        ))
