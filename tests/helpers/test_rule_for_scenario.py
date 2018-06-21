from voximplant_client import helpers


def test_rule_for_scenario():
    assert helpers.get_rule_name_for_scenario('test.js') == 'auto-rule-test'
