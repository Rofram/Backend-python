from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """
        Returns the engine
        :params: None
        :return: engine
        """

        engine = create_engine(self.__connection_string)

        return engine

    def __enter__(self):
        """
        Returns the session
        :params: None
        :return: session
        """

        engine = self.get_engine()
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the session
        :params: None
        :return: None
        """

        if self.session is not None:
            self.session.close()
