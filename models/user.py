#!/usr/bin/python3

"""

This module defines a User Class

"""

from .base_model import BaseModel


class User(BaseModel):
    """
    A User Class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
