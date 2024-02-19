from jose import jwt

from fast_zero.security import SECRET_KEY, creat_access_token


def test_jwt():
    data = {'test': 'test'}
    token = creat_access_token(data)

    decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']
