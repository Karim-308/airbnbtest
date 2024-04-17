#!/usr/bin/python3
"""Defines the City class."""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

class City(BaseModel, Base):
    """Represents a city for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table 'cities'.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (Column): The name of the City.
        state_id (Column): The state id of the City.
        places (relationship): Relationship to Place model.
    """
    __tablename__ = "cities"
    
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="city", cascade="delete")
