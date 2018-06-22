def test_ok(client, runner, cli):
    def assertions(request, *args):
        assert 'rewrite=True' in request.text
        assert 'scenario_name=test.js' in request.text
        assert 'fuck' in request.text  # this was in the JS file

        return {}

    client.m.post('https://api.host.com/AddScenario/', json=assertions)

    result = runner.invoke(cli.upload, ['./tests/.fixtures/test.js'], obj=client)

    assert 'OK' in result.output


def test_error(client, runner, cli):
    client.m.post('https://api.host.com/AddScenario/', json={'error': {'msg': '__mocked_error_msg__'}})

    result = runner.invoke(cli.upload, ['./tests/.fixtures/test.js'], obj=client)
    assert '__mocked_error_msg__' in result.output
