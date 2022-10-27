#!/usr/bin/python3
"""class Reviews"""


from models.base_model import BaseModel


class Review(BaseModel):
   """reps a review"""
   place_id = ""
   user_id = ""
   text = ""
   