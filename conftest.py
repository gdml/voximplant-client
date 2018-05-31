from os import path

import pytest
import requests_mock
import simplejson as json

from voximplant_client import VoximplantClient


@pytest.fixture
def client():
    """Configured instance of Voximplant Client"""
    return VoximplantClient(
        host='https://api.host.com:6800',
        account_id='100500',
        api_key='b76e5c4f-16b5-47ea-9f92-999815dd3797',
    )


@pytest.fixture
def mocked_http_client(client, response):
    """Client with blocked requests and requests_mock injected to .m"""
    with requests_mock.Mocker() as m:
        client.m = m
        yield client


@pytest.fixture
def response():
    """Fixture reader"""
    def read_file(f):
        with open(path.join('tests/fixtures/', f) + '.json') as fp:
            return json.load(fp)

    return read_file
