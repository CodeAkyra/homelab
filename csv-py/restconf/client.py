import requests
from config import DEVICE, HEADERS

requests.packages.urllib3.disable_warnings()


def get_interfaces():
    url = f"{DEVICE['host']}/restconf/data/ietf-interfaces:interfaces"

    response = requests.get(
        url,
        auth=(DEVICE["username"], DEVICE["password"]),
        headers=HEADERS,
        verify=False,
    )

    response.raise_for_status()
    return response.json()
