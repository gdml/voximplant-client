import pytest

from voximplant_client import exceptions

VALID_APP = 'testapp.testclient.voximplant.com'


def test_list(client):
    got = client.queues.list(VALID_APP)

    assert len(got.result) == 2


def test_bad_app_name(client):
    with pytest.raises(exceptions.VoximplantBadApplicationNameException):
        client.queues.list('noapp.noclient.voximplant.com')
