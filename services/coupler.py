import os
import httpx

SYMBOL_SERVICE_HOST_URL = 'http://10.0.2.11:8000/symbols/'

def is_symbol_present(symbol_id: int):
    url = os.environ.get('SYMBOL_SERVICE_HOST_URL') or SYMBOL_SERVICE_HOST_URL
    r = httpx.get(f'{url}{symbol_id}')
    return True if r.status_code == 200 else False


def symbol_to_bind(symbol: str):
    api = os.environ.get('SYMBOL_SERVICE_HOST_URL') or SYMBOL_SERVICE_HOST_URL
    url = f'bind/{str}'

