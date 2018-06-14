import pytest

from voximplant_client import VoximplantClient


@pytest.fixture
def client():
    return lambda host: VoximplantClient('100500', 's3c3rt', host)


@pytest.mark.parametrize('host, url, expected', [
    ['https://api.com:6800', 'test/create', 'https://api.com:6800/test/create/?account_id={account_id}&api_key={api_key}'],
    ['https://api.com:6800/', 'test/create', 'https://api.com:6800/test/create/?account_id={account_id}&api_key={api_key}'],
    ['https://api.com:6800/', '/test/create', 'https://api.com:6800/test/create/?account_id={account_id}&api_key={api_key}'],
    ['https://api.com:6800/v1', '/test/create', 'https://api.com:6800/v1/test/create/?account_id={account_id}&api_key={api_key}'],
    ['https://api.com:6800/v1/', '/test/create', 'https://api.com:6800/v1/test/create/?account_id={account_id}&api_key={api_key}'],
    ['https://api.com:6800/v1', 'test/create', 'https://api.com:6800/v1/test/create/?account_id={account_id}&api_key={api_key}'],
])
def test_format_url(client, host, url, expected, monkeypatch):
    client = client(host)
    assert client.http.format_url(url) == expected.format(account_id=client.http.account_id, api_key=client.http.api_key)
