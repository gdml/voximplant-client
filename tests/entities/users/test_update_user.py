import pytest

from voximplant_client import exceptions


def test_update_ok(client, response):
    client.m.post('https://api.host.com/SetUserInfo/', json=response('UserOk'))

    got = client.users.update(
        'testapp.testclient.voximplant.com',
        'crazyjohn1989',
        user_active=False,
    )

    assert not got.isError
    assert got['user_id'] == 100500


def test_bad_application_name(client):
    with pytest.raises(exceptions.VoximplantBadApplicationNameException):
        client.users.update(
            'noapp.noclient.voximplant.com',
            'crazyjohn1989',
            user_active=False,
        )


def test_bad_response(client, response):
    client.m.post('https://api.host.com/SetUserInfo/', json=response('BadUser'))

    got = client.users.update(
        'testapp.testclient.voximplant.com',
        'crazyjohn1989',
        user_active=False,
    )

    assert got.isError
