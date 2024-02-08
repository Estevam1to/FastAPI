import textwrap


def test_root(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_mundo(client):
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


def test_create_user(client):
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


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'username': 'vasco',
                'email': 'vascodagama@exemplo.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'vasco',
            'email': 'vascodagama@exemplo.com',
            'password': 'vascocampeao',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'vasco',
        'email': 'vascodagama@exemplo.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'message': 'User deleted'}


# teste erro 404 delete_user
def test_update_user_404(client):
    response = client.put(
        '/users/-1',
        json={
            'username': 'vasco',
            'email': 'vascodagama@exemplo.com',
            'password': 'vascocampeao',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


# teste erro 404 delete_user
def test_delete_user_404(client):
    response = client.delete('/users/-1')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
