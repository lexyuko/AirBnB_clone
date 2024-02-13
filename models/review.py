#!/usr/bin/python3
"""define a class Review"""

from models.base_model import BaseModel
class Review:
    """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
