from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/mundo', status_code=200, response_class=HTMLResponse)
def ola_mundo_html():
    return """<!DOCTYPE html>
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


# banco provisório
database = []

# decorador que define o endpoint que receberá usuários
@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(User.username) == user.username
    )

    if db_user:
        raise HTTPException(
            status_code=404, detail='Username already registered'
        )

    db_user = User(
        username=user.username, password=user.password, email=user.email
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1 or database[user_id - 1] is None:
        raise HTTPException(status_code=404, detail='User not found')

    user_with_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id

    return UserPublic(id=user_id, username=user.username, email=user.email)


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1 or database[user_id - 1] is None:
        raise HTTPException(status_code=404, detail='User not found')

    del database[user_id - 1]

    return {'message': 'User deleted'}


@app.get('/user/{user_id}')
def read_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')

    return {'user': database[user_id - 1]}
