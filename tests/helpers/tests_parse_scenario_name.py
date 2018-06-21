import pytest

from voximplant_client import helpers


@pytest.mark.parametrize('input, expected', [
    ['app/scenario', ('app', 'scenario')],
    ['app/scenario/bullshit', ('app', 'scenario')],
    ['scenario', (None, 'scenario')],
])
def test(input, expected):
    assert helpers.parse_scenario_name(input) == expected
