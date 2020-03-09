import pytest


@pytest.fixture(autouse=True)
def mocked_get_call_history(client, response):
    return client.m.get('https://api.host.com/GetCallHistory/', json=response('GetCallHistory'))


@pytest.fixture(autouse=True)
def mocked_get_application(client, response):
    client.m.get('https://api.host.com/GetApplications/', json=response('GetApplications'))
