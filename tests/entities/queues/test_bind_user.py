import pytest

from voximplant_client import exceptions


def test_binding_ok(client, response):
    client.m.post('https://api.host.com/BindUserToQueue/', json=response('BindUserOk'))

    got = client.queues.bind_user(
        'testapp.testclient.voximplant.com',
        'support',
        'jd1',
        bind=False,
    )

    assert not got.isError


def test_binding_params(client):
    def assertions(request, *args):
        assert 'application_id=4379769'in request.text
        assert 'user_id=200500'in request.text
        assert 'acd_queue_id=3345'in request.text
        assert 'bind=False'in request.text

        return {}

    client.m.post('https://api.host.com/BindUserToQueue/', json=assertions)
    client.queues.bind_user(
        'testapp.testclient.voximplant.com',
        'support',
        'jd1',
        bind=False,
    )


def test_bad_application_name(client):
    with pytest.raises(exceptions.VoximplantBadApplicationNameException):
        client.queues.bind_user(
            'non-existant.testclient.voximplant.com',
            'support',
            'jd1',
            bind=False,
        )


def test_user_does_not_exist(client):
    with pytest.raises(exceptions.VoximplantUserDoesNotExistsException):
        client.queues.bind_user(
            'testapp.testclient.voximplant.com',
            'support',
            'crazyjohn1989',
            bind=False,
        )


def test_queue_does_not_exist(client):
    with pytest.raises(exceptions.VoximplantQueueDoesNotExistsException):
        client.queues.bind_user(
            'testapp.testclient.voximplant.com',
            'non-existant',
            'jd1',
            bind=False,
        )


def test_bad_response(client, response):
    client.m.post('https://api.host.com/BindUserToQueue/', json=response('BindUserFail'))

    with pytest.raises(exceptions.VoximplantQueueBindException):
        client.queues.bind_user(
            'testapp.testclient.voximplant.com',
            'support',
            'jd1',
            bind=False,
        )
