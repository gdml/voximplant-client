import pytest

from voximplant_client import exceptions


@pytest.mark.parametrize('method, call', [
    ['get', lambda client: client.http.get('endpoint')],
    ['post', lambda client: client.http.post('endpoint', {})],
])
def test_auth_params(client, method, call):
    """Make sure given methods pass authentication parameters in the querystring"""
    def param_assertions(request, *args):
        assert 'account_id=100500' in request.url
        assert 'api_key=secret' in request.url

        return {}

    getattr(client.m, method)('https://api.host.com/endpoint/', json=param_assertions)
    call(client)


def test_get(client, response):
    client.m.get('https://api.host.com/GetApplications/', json=response('GetApplications'))

    got = client.http.get('GetApplications')

    assert len(got.result) == 2


def test_non_200_get(client):
    client.m.get('https://api.host.com/GetApplications/', status_code=402)

    with pytest.raises(exceptions.VoxImplantClientException):
        client.http.get('GetApplications')


def test_get_list(client, monkeypatch):
    monkeypatch.setattr(client.http, 'DEFAULT_COUNT', 100500)

    def param_assertions(request, *args):
        assert 'count=100500' in request.url
        return {}

    client.m.get('https://api.host.com/GetApplications/', json=param_assertions)
    client.http.get_list('GetApplications')


def test_post(client, response):
    client.m.post('https://api.host.com/AddScenario/', json=response('ScenarioOk'))

    got = client.http.post('AddScenario', {'scenario_name': 'test.js', 'scenario_script': 'console.log([] == ![])'})

    assert got.isError is False
    assert got['scenario_id'] == 1134324


def test_post_non_201(client):
    client.m.post('https://api.host.com/AddScenario/', status_code=403)

    with pytest.raises(exceptions.VoxImplantClientException):
        client.http.post('AddScenario', {})


def test_post_non_ok_response(client, response):
    client.m.post('https://api.host.com/AddScenario/', json=response('ScenarioIsNotUnique'))

    got = client.http.post('AddScenario', {'scenario_name': 'test.js', 'scenario_script': 'console.log(NaN === NaN)'})

    assert got.isError is True
