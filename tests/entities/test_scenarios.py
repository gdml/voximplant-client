def test_list(client, response):
    client.m.get('https://api.host.com/GetScenarios/', json=response('GetApplications'))  # i realy use another fixture cuz it does not matter here

    got = client.scenarios.list()

    assert len(got.result) == 2


def test_adding(client, response):
    def assertions(request, *args):
        assert 'rewrite=True' in request.text
        assert 'scenario_name=test.js' in request.text
        assert 'fuck' in request.text  # this was in the JS file

        return {}

    client.m.post('https://api.host.com/AddScenario/', json=assertions)
    client.scenarios.add('test.js', './tests/.fixtures/test.js')
