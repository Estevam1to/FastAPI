from sqlalchemy import select

from fast_zero.models import Todo, User


def test_create_user(session):
    new_user = User(username='Estevam', password='teste', email='tesye@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'Estevam'))

    assert user.username == 'Estevam'


def test_create_todo(session, user: User):
    todo = Todo(
        title='Test Todo',
        description='Test Desc',
        state='draft',
        user_id=user.id,
    )

    session.add(todo)
    session.commit()
    session.refresh(todo)

    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos
