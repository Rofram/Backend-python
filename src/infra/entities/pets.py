import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """
    Enum for animal types
    """

    CAT = "cat"
    DOG = "dog"
    BIRD = "bird"
    FISH = "fish"
    TURTLE = "turtle"


class Pets(Base):
    """
    This class represents the Pets table.
    """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return (
            f"Pet: [name: {self.name}, specie: {self.specie}, user_id: {self.user_id}]"
        )
