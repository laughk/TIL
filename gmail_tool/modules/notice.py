import requests


def post_by_incoming_webhook(base: list, endpoint: str) -> None:
    payload = {'blocks': base}
    requests.request(
        'POST', json=payload, url=endpoint,
    )
