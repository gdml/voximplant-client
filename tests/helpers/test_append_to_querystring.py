import pytest

from voximplant_client import helpers


@pytest.mark.parametrize('input, expected', [
    ['/test/create', '/test/create/?password=lovesecretgod'],
    ['/test/create/', '/test/create/?password=lovesecretgod'],
    ['/test/create/?par=val', '/test/create/?par=val&password=lovesecretgod'],
    ['/test/create/?par=val&par1=val1', '/test/create/?par=val&par1=val1&password=lovesecretgod'],
])
def test_single_kwarg(input, expected):
    assert helpers.append_to_querytring(input, password='lovesecretgod') == expected


def test_mulitple_kwargs():
    got = helpers.append_to_querytring('/test/create', login='z3r0c00l', password='lovesecretgod')

    assert 'login=z3r0c00l' in got
    assert 'password=lovesecretgod' in got
