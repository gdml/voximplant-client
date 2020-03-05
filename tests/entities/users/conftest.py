import pytest


@pytest.fixture
def client(client, response):
    client.m.get('https://api.host.com/GetApplications/', json=response('GetApplications'))
    client.m.get('https://api.host.com/GetUsers/', json=response('GetUsers'))

    return client
