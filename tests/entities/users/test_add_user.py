import pytest

from voximplant_client import exceptions


def test_adding_ok(client, response):
    client.m.post('https://api.host.com/AddUser/', json=response('UserOk'))

    got = client.users.add(
        'testapp.testclient.voximplant.com',
        'crazyjohn1989',
        'John Doe',
        's3CreT',
    )

    assert not got.isError
    assert got['user_id'] == 100500


def test_bad_application_name(client):
    with pytest.raises(exceptions.VoximplantBadApplicationNameException):
        client.users.add(
            'noapp.noclient.voximplant.com',
            'crazyjohn1989',
            'John Doe',
            's3CreT',
        )


def test_bad_response(client, response):
    client.m.post('https://api.host.com/AddUser/', json=response('BadUser'))

    got = client.users.add(
        'testapp.testclient.voximplant.com',
        'crazyjohn1989',
        'John Doe',
        's3CreT',
    )

    assert got.isError
