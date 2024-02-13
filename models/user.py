#!/usr/bin/python3
"""define a class User"""
from models.base_model import BaseModel

class User:
    """Represent a User
    Attributes:
        email (str): the email of a user
        password(str): the password of a user
        first_name (str): the first name of the user
        last_name (str): the last of name of the user
        """

    email = ""
    password = ""
    first_name = ""
    last_name = ""