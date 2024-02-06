import textwrap

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_mundo():
    client = TestClient(app)

    response = client.get('/mundo')

    assert response.status_code == 200
    expected_content = """<!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title> Tarefa 1 </title>
        </head>
        <body>
            <h1> Olá Mundo!</h1>
            <p> Estevam lindão </p>
        </body>
        </html>"""

    assert ''.join(response.content.decode('utf-8').split()) == ''.join(
        textwrap.dedent(expected_content).strip().split()
    )


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'vasco',
            'email': 'vascodagama@exemplo.com',
            'password': 'vascocampeao',
        },
    )

    assert response.status_code == 201  # created

    assert response.json() == {
        'username': 'vasco',
        'email': 'vascodagama@exemplo.com',
        'id': 1,
    }
