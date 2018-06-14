import pytest

from voximplant_client import exceptions


@pytest.fixture
def client(client, response):
    client.m.get('https://api.host.com/GetApplications/', json=response('GetApplications'))

    return client


def test_list(client, response):
    client.m.get('https://api.host.com/GetRules/', json=response('GetRules'))

    got = client.rules.list('testapp.testclient.voximplant.com')

    assert len(got.result) == 2


def test_bad_app_name(client):
    with pytest.raises(exceptions.VoxImplantBadApplicationNameException):
        client.rules.list('noapp.noclient.voximplant.com')
