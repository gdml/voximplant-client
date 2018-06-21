import pytest

from voximplant_client import exceptions


@pytest.fixture
def client(client, response):
    client.m.get('https://api.host.com/GetApplications/', json=response('GetApplications'))
    client.m.get('https://api.host.com/GetRules/', json=response('GetRules'))

    client.m.post('https://api.host.com/AddRule/', json=response('RuleOk'))  # adding rule

    return client


def test_running_existing_scenario(client, response):
    client.m.post('https://api.host.com/StartScenarios/', json=response('ScenarioRunOk'))
    result = client.scenarios.start('testapp.testclient.voximplant.com/test_fetching_order1')

    assert not result.isError
    assert 'media_session_access_url' in result


def test_running_new_scenario(client, response):
    def assertions(request, *args):
        assert 'rule_id=1808186' in request.text  # correct_rule_id

        return {}

    client.m.post('https://api.host.com/StartScenarios/', json=assertions)

    client.scenarios.start('testapp.testclient.voximplant.com/newscenario.js')


@pytest.mark.parametrize('scenario', [
    'noexistant.app/newscenario.js',
    'newscenario.js',
])
def test_bad_application_name(scenario, client):
    with pytest.raises(exceptions.VoximplantBadApplicationNameException):
        client.scenarios.start(scenario)
