from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Users(Base):
    """Users entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    id_pet = relationship("Pets")

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __rep__(self) -> str:
        return f"User [name={self.name}]"
