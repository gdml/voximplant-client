import pytest

from voximplant_client import exceptions

VALID_APP = 'testapp.testclient.voximplant.com'


def test_list(client):
    got = client.rules.list(VALID_APP)

    assert len(got.result) == 2


def test_bad_app_name(client):
    with pytest.raises(exceptions.VoximplantBadApplicationNameException):
        client.rules.list('noapp.noclient.voximplant.com')


def test_list_cache_is_stored(client, monkeypatch):
    monkeypatch.setattr(client.rules, 'list', lambda *args: '__m0ck__')

    assert client.rules._get_cached_rules_list(VALID_APP) == '__m0ck__'
    assert client.rules._rule_cache[VALID_APP] == '__m0ck__'


def test_list_cache_is_used(client):
    client.rules._rule_cache[VALID_APP] = '__m0ck__'
    assert client.rules._get_cached_rules_list(VALID_APP) == '__m0ck__'
