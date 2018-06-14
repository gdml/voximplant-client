import pytest

from voximplant_client import exceptions


def test_get(client, response):
    client.m.get('https://api.host.com/GetApplications/', json=response('GetApplications'))

    got = client.http.get('GetApplications')

    assert len(got.result) == 2


def test_non_200_get(client, response):
    client.m.get('https://api.host.com/GetApplications/', status_code=402)

    with pytest.raises(exceptions.VoxImplantClientException):
        client.http.get('GetApplications')
