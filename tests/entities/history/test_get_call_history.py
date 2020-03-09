from datetime import datetime

import pytest

from voximplant_client import exceptions


def test(client):
    got = client.history.get_call_history()

    assert len(got.result) == 3


def test_converting_datetime(client, mocked_get_call_history):
    client.history.get_call_history(
        from_date=datetime(2019, 3, 2, 22, 23, 21),
        to_date=datetime(2020, 3, 2, 22, 23, 21),
    )

    assert mocked_get_call_history.last_request.qs['from_date'][0] == '2019-03-02 22:23:21'
    assert mocked_get_call_history.last_request.qs['to_date'][0] == '2020-03-02 22:23:21'


@pytest.mark.parametrize('call_session_history_id, expected', (
    ((123, 456, 789), '123;456;789;'),
    ((123,), '123;'),
))
def test_converting_call_session_history_id(client, mocked_get_call_history, call_session_history_id, expected):
    client.history.get_call_history(
        call_session_history_id=call_session_history_id,
    )

    assert f'call_session_history_id={expected}&' in mocked_get_call_history.last_request.query


def test_converting_app(client, mocked_get_call_history):
    client.history.get_call_history(
        app='testapp.testclient.voximplant.com',
    )

    assert mocked_get_call_history.last_request.qs['application_id'][0] == '4379769'


def test_default_args(client, mocked_get_call_history):
    client.history.get_call_history(
        app='testapp.testclient.voximplant.com',
    )

    assert mocked_get_call_history.last_request.qs['with_calls'][0] == 'true'
    assert mocked_get_call_history.last_request.qs['with_records'][0] == 'false'
    assert mocked_get_call_history.last_request.qs['count'][0] == '20'
    assert mocked_get_call_history.last_request.qs['offset'][0] == '0'


def test_query_does_not_have_null_args(client, mocked_get_call_history):
    client.history.get_call_history()

    assert 'from_date' not in mocked_get_call_history.last_request.qs.keys()
    assert 'to_date' not in mocked_get_call_history.last_request.qs.keys()
    assert 'call_session_history_id' not in mocked_get_call_history.last_request.qs.keys()
    assert 'app' not in mocked_get_call_history.last_request.qs.keys()


def test_bad_application_name(client):
    with pytest.raises(exceptions.VoximplantBadApplicationNameException):
        client.history.get_call_history(
            app='noapp.noclient.voximplant.com',
        )
