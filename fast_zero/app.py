from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=(len(database) + 1))

    database.append(user_with_id)

    return UserPublic(
        id=user_with_id.id, username=user.username, email=user.email
    )


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}
