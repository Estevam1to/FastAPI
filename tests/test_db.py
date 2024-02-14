from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(username='Estevam', password='teste', email='tesye@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'Estevam'))

    assert user.username == 'Estevam'
