import pytest

from voximplant_client import exceptions

VALID_APP = 'testapp.testclient.voximplant.com'


@pytest.mark.parametrize('scenario, rule_id', [
    ['test_fetching_order1', 1770572],
    ['nonexisting_scenario', None],
])
def test_get_rule_for_scenario(client, scenario, rule_id):
    assert client.rules.get_for_scenario(app=VALID_APP, scenario=scenario) == rule_id


@pytest.mark.parametrize('scenario, rule_id', [
    ['test_fetching_order1', 1770572],
    ['nonexisting_scenario', 1808186],
])
def test_get_or_create(client, scenario, rule_id, response):
    client.m.post('https://api.host.com/AddRule/', json=response('RuleOk'))

    assert client.rules.get_or_create_for_scenario(app=VALID_APP, scenario=scenario) == rule_id


def test_rule_creation_error(client, response):
    client.m.post('https://api.host.com/AddRule/', json=response('BadScenario'))

    with pytest.raises(exceptions.VoximplantRuleCreationError):
        client.rules.get_or_create_for_scenario(app=VALID_APP, scenario='test.js')
