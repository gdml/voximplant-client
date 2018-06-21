import pytest

from voximplant_client import exceptions

VALID_APP = 'testapp.testclient.voximplant.com'


@pytest.mark.parametrize('rule_identifier', [
    {'name': 'auto-rule-test_fetching_order1'},
    {'id': 1770572},
])
def test_ok(client, response, rule_identifier):
    client.m.post('https://api.host.com/BindScenario/', json=response('BindScenarioOk'))

    result = client.rules.bind_scenario(VALID_APP, 'test.js', **rule_identifier)

    assert not result.isError


def test_binding_fail(client, response):
    client.m.post('https://api.host.com/BindScenario/', json=response('BindScenarioFail'))
    result = client.rules.bind_scenario(VALID_APP, 'test.js', id=1770572)

    assert result.isError


def test_bad_rule_name(client):
    with pytest.raises(exceptions.VoximplantBadRuleNameException):
        client.rules.bind_scenario(VALID_APP, 'test.js', name='invalid-rule')


def test_bad_id(client):
    with pytest.raises(exceptions.VoximplantBadRuleId):
        client.rules.bind_scenario(VALID_APP, 'test.js', id=1005000)  # invalid
