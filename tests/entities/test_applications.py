import pytest


@pytest.fixture
def client(client, response):
    client.m.get('https://api.host.com/GetApplications/', json=response('GetApplications'))
    return client


def test_list(client):
    got = client.applications.list()

    assert len(got.result) == 2


@pytest.mark.parametrize('app_name, id', [
    ['testapp.testclient.voximplant.com', 4379769],
    ['testapp1.testclient.voximplant.com', 4379770],
    ['noapp.noclient.voximplant.com', None],
])
def test_get_id(client, app_name, id):
    assert client.applications.get_id(app_name) == id
