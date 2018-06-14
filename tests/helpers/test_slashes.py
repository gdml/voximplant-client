import pytest

from voximplant_client import helpers


@pytest.mark.parametrize('input, expected', [
    ['/a', '/a'],
    ['a', '/a'],
])
def test_prepend_slash(input, expected):
    assert helpers.prepend_slash(input) == expected


@pytest.mark.parametrize('input, expected', [
    ['a/', 'a/'],
    ['a', 'a/'],
])
def test_append_slash(input, expected):
    assert helpers.append_slash(input) == expected


@pytest.mark.parametrize('input, expected', [
    ['a/', 'a'],
    ['a', 'a'],
])
def test_remove_trailing_slash(input, expected):
    assert helpers.remove_trailing_slash(input) == expected
