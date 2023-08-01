import requests
import json

from pytest_bdd import scenarios, given, then, parsers

# Shared Variables

API = 'https://api.publicapis.org/entries'

# Scenarios
scenarios('../features/service.feature')

CONVERTERS = {
    'code': int,
    'phrase': str,
}


# Given Steps

@given(
    parsers.parse('the API is queried with "{phrase}"'),
    target_fixture='ddg_response',
    converters=CONVERTERS)
def ddg_response(phrase):
    response = requests.get(API)
    print('given response', response)
    return response


# Then Steps
@then(
    parsers.parse('the response status code is "{code}"'),
    converters=CONVERTERS)
def ddg_response_code(ddg_response, code):
    print('get response', ddg_response.json()['count'])
    assert ddg_response.status_code == code


@then(
    parsers.parse('the response contains results for "{phrase}"'),
    converters=CONVERTERS)
def ddg_response_contents(ddg_response, phrase):
    assert phrase.lower() != ddg_response.json()
    print("Response json->>", json.dumps(ddg_response.json(), indent=2))
