from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

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


# decorador que define o endpoint que receberá usuários
@app.post('/users/', status_code=201)
def create_user():
    pass
