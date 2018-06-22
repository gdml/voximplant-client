import pytest
from click.testing import CliRunner


@pytest.fixture
def client(client, response):
    client.m.get('https://api.host.com/GetApplications/', json=response('GetApplications'))
    client.m.get('https://api.host.com/GetRules/', json=response('GetRules'))

    return client


@pytest.fixture
def runner():
    """Click test runner"""
    return CliRunner(env=dict(
        VOXIMPLANT_ACCOUNT_ID='1006001',
        VOXIMPLANT_API_KEY='s3cr37',
    ))


@pytest.fixture
def cli():
    from voximplant_client import cli
    return cli
