#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User model
    
    Class_Attributes:
        email: User email
        password: user password
        first_name: User first name
        last_name: User last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""