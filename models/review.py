#!/usr/bin/python3

"""

This module defines a Review Class

"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    A Review Class
    """
    place_id = ''
    user_id = ''
    text = ''
