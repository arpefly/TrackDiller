import requests

from utils.config import exchangerate_API


def convert() -> tuple[int, int]:
    return (
        requests.get(f'https://v6.exchangerate-api.com/v6/{exchangerate_API}/latest/PLN').json()['conversion_rates']['USD'],
        requests.get(f'https://v6.exchangerate-api.com/v6/{exchangerate_API}/latest/EUR').json()['conversion_rates']['USD']
    )
