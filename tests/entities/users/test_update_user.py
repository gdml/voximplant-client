import pytest

from voximplant_client import exceptions


def test_update_ok(client, response):
    client.m.post('https://api.host.com/SetUserInfo/', json=response('UserOk'))

    got = client.users.update(
        'testapp.testclient.voximplant.com',
        'jd1',
        user_active=False,
    )

    assert not got.isError


def test_updating_params(client):
    def assertions(request, *args):
        assert 'application_id=4379769'in request.text
        assert 'user_name=jd1'in request.text
        assert 'some_stuff=doing-it-right'in request.text

        return {}

    client.m.post('https://api.host.com/SetUserInfo/', json=assertions)
    client.users.update(
        'testapp.testclient.voximplant.com',
        'jd1',
        some_stuff='doing-it-right',
    )


def test_bad_application_name(client):
    with pytest.raises(exceptions.VoximplantBadApplicationNameException):
        client.users.update(
            'noapp.noclient.voximplant.com',
            'jd1',
            user_active=False,
        )


def test_bad_response(client, response):
    client.m.post('https://api.host.com/SetUserInfo/', json=response('BadUser'))

    with pytest.raises(exceptions.VoximplantUserUpdateException):
        client.users.update(
            'testapp.testclient.voximplant.com',
            'jd1',
            user_active=False,
        )


def test_user_does_not_exists(client):
    with pytest.raises(exceptions.VoximplantUserDoesNotExistsException):
        client.users.update(
            'testapp.testclient.voximplant.com',
            'crazyjohn1989',
            user_active=False,
        )
