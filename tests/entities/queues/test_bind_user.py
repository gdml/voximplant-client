import pytest

from voximplant_client import exceptions


def test_binding_ok(client, response):
    client.m.post('https://api.host.com/BindUserToQueue/', json=response('BindUserOk'))

    got = client.queues.bind_user(
        'testapp.testclient.voximplant.com',
        'jd1',
        'support',
        bind=False,
    )

    assert not got.isError


def test_bad_application_name(client):
    with pytest.raises(exceptions.VoximplantBadApplicationNameException):
        client.queues.bind_user(
            'non-existant.testclient.voximplant.com',
            'jd1',
            'support',
            bind=False,
        )


def test_user_does_not_exist(client):
    with pytest.raises(exceptions.VoximplantUserDoesNotExistsException):
        client.queues.bind_user(
            'testapp.testclient.voximplant.com',
            'crazyjohn1989',
            'support',
            bind=False,
        )


def test_queue_does_not_exist(client):
    with pytest.raises(exceptions.VoximplantQueueDoesNotExistsException):
        client.queues.bind_user(
            'testapp.testclient.voximplant.com',
            'jd1',
            'non-existant',
            bind=False,
        )


def test_bad_response(client, response):
    client.m.post('https://api.host.com/BindUserToQueue/', json=response('BindUserFail'))

    with pytest.raises(exceptions.VoximplantQueueBindException):
        client.queues.bind_user(
            'testapp.testclient.voximplant.com',
            'jd1',
            'support',
            bind=False,
        )
