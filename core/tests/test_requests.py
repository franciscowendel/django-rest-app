import requests


def test_get():
    avaliacoes = requests.get('http://127.0.0.1:8000/api/v1/avaliacoes/')

    print(avaliacoes.status_code)
