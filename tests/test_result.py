import pytest

from voximplant_client.result import VoximplantAPIResult


@pytest.fixture
def result(response):
    return lambda fixture: VoximplantAPIResult(response(fixture))


def test_result(result):
    got = result('GetApplications')

    assert len(got.result) == 2


def test_no_result(result):
    got = result('error')

    assert got.result == []


@pytest.mark.parametrize('fixture, isError', [
    ['GetApplications', False],
    ['error', True],
])
def test_is_error(result, fixture, isError):
    got = result(fixture)

    assert got.isError is isError
