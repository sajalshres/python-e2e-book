"""A requests library example"""

import requests
from requests.exceptions import HTTPError

github_api = "https://api.github.com"

headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

data = None

try:
    response = requests.get(
        url = github_api,
        headers = headers,
        verify = False
    )

    response.raise_for_status()

    if response.status_code == 200:
        data = response.json()

except HTTPError as http_error:
    print(f"HTTP error occurred: {http_error}")
except Exception as error:
    print(f"Some other error occurred: {error}")

if data:
    print(data)
