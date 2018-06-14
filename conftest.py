from os import path

import pytest
import requests_mock
import simplejson as json

from voximplant_client import VoximplantClient


@pytest.fixture
def pure_client():
    """Configured instance of Voximplant Client"""
    return VoximplantClient(
        host='https://api.host.com',
        account_id='100500',
        api_key='secret',
    )


@pytest.fixture
def client(pure_client, response):
    """Client with blocked requests and requests_mock injected to .m"""
    with requests_mock.Mocker() as m:
        pure_client.m = m
        yield pure_client


@pytest.fixture
def response():
    """Fixture reader"""
    def read_file(f):
        with open(path.join('tests/.fixtures/', f) + '.json') as fp:
            return json.load(fp)

    return read_file
