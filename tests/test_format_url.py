import pytest


@pytest.mark.parametrize('host, url, expected', [
    ['https://api.com:6800', 'test/create', 'https://api.com:6800/test/create/?account_id={account_id}&api_key={api_key}'],
    ['https://api.com:6800/', 'test/create', 'https://api.com:6800/test/create/?account_id={account_id}&api_key={api_key}'],
    ['https://api.com:6800/', '/test/create', 'https://api.com:6800/test/create/?account_id={account_id}&api_key={api_key}'],
])
def test_format_url(client, host, url, expected, monkeypatch):
    monkeypatch.setattr(client, 'host', host)
    assert client.format_url(url) == expected.format(account_id=client.account_id, api_key=client.api_key)
