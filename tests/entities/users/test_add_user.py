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


def test_adding_params(client):
    def assertions(request, *args):
        assert 'application_id=4379769'in request.text
        assert 'user_name=crazyjohn1989'in request.text
        assert 'user_display_name=John+Doe'in request.text
        assert 'user_password=s3CreT'in request.text

        return {}

    client.m.post('https://api.host.com/AddUser/', json=assertions)
    client.users.add(
        'testapp.testclient.voximplant.com',
        'crazyjohn1989',
        'John Doe',
        's3CreT',
    )


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

    with pytest.raises(exceptions.VoximplantUserCreationException):
        client.users.add(
            'testapp.testclient.voximplant.com',
            'crazyjohn1989',
            'John Doe',
            's3CreT',
        )


def test_user_already_exists(client):
    with pytest.raises(exceptions.VoximplantUserAlreadyExistsException):
        client.users.add(
            'testapp.testclient.voximplant.com',
            'jd1',
            'John Doe',
            's3CreT',
        )
