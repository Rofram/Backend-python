from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakeRepo:
    """Simple fake Repository"""

    @classmethod
    def insert_user(cls) -> None:
        """Insert a user in the database"""
        with DBConnectionHandler() as connection:
            try:
                new_user = Users(name="Rodrigo", password="Rodrigo123")
                connection.session.add(new_user)
                connection.session.commit()
            except Exception as e:
                connection.session.rollback()
                raise e
            finally:
                connection.session.close()
