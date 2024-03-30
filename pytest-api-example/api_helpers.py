import requests

base_url = 'http://localhost:5000'

# GET requests


def get_api_data(endpoint, params={}):
    print(f"\nRequest\n-------\nEndpoint: {base_url}{endpoint}")
    print(f"Body: {params}")
    response = requests.get(f'{base_url}{endpoint}', params=params)
    return response

# POST requests


def post_api_data(endpoint, data):
    print(f"\nEndpoint: {base_url}{endpoint}")
    print(f"Body: {data}")
    response = requests.post(f'{base_url}{endpoint}', json=data)
    return response

# PATCH requests


def patch_api_data(endpoint, data):
    print(f"\nEndpoint: {base_url}{endpoint}")
    print(f"Body: {data}")
    response = requests.patch(f'{base_url}{endpoint}', json=data)
    return response
