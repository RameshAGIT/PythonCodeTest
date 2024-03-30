import json
import uuid
import pytest
import api_helpers


@pytest.fixture
def generate_Order_id():
    return str(uuid.uuid4())


def printRequestPayload(data, resource):
    print("\nRequest payload:")
    print(json.dumps(data, indent=4))
    print(f"\nEndpoint: {api_helpers.base_url}{resource}")


def printResponsePayload(response):
    responsePayload = response.json()
    print(f"\nResponse\n--------")
    print(f'Header: {response.headers}')
    print(f'StatusCode: {response.status_code}')
    print(f'Body: {response.text}')
    return responsePayload
