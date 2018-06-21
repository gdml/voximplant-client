import pytest

from voximplant_client import exceptions


def test_adding_ok(client, response):
    client.m.post('https://api.host.com/AddRule/', json=response('RuleOk'))

    got = client.rules.add(
        app='testapp.testclient.voximplant.com',
        scenario='test.js',
    )

    assert not got.isError
    assert got['rule_id'] == 1808186


def test_bad_application_name(client):
    with pytest.raises(exceptions.VoxImplantBadApplicationNameException):
        client.rules.add(
            app='noapp.noclient',
            scenario='test.js',
        )


def test_bad_response(client, response):
    client.m.post('https://api.host.com/AddRule/', json=response('BadScenario'))

    got = client.rules.add(
        app='testapp.testclient.voximplant.com',
        scenario='test.js',
    )

    assert got.isError
