# Python client for voximplant.com HTTP API

This is a simple client for [voximplant.com](https://voximplant.com) HTTP API. It is intended for ad-hoc scenario running and uploading, but may simple be used for any manipulations.

## Installation

```sh
$ pip install voximplant_client
```

## CLI Usage

WIP yet

## Programmatic Usage

First, you should get your API key at [voximplant management interface](https://manage.voximplant.com/#apiaccess).

```python
from voximplant_client import VoximplantClient

client = VoximplantClient(
  account_id='<YOUR_ACCOUNT_ID>'
  api_key='<YOUR_API_KEY>'
)
```


Deploying a scenario:

```python
  client.scenarios.add('test.js', path='./path/to/scenario.js')
  
  # or directly upload a code
  
  with open('./path/to/scenario.js') as f:
     client.scenarios.add('test.js', code=f.read())
```


Running a scenario inside the app (the required rule will be created automaticaly):

```python
client.scenarios.start('app.client.voximplat.com/test.js')  # app_name/scenario_name
```

Running random queries for the API:

```python
skills = client.http.get('GetSkills')

for skill in skills.result:
  print(f"{skill['id']: skill['name']")
  
# upload new skill

client.http.post('AddSkill', dict(
	skill_name='joking',
))
```