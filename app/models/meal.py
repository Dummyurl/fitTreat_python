'''
Meal Model
Created on 18-Dec-2018

@author= Balkrishna.Meena
'''
from flask_mongoengine import Document
from mongoengine.fields import StringField, IntField
from mongoengine.base.fields import BaseField
from mongoengine.fields import ListField


class Meals(Document):
    name = StringField(required=True, unique=True)
    foodPreference = BaseField(default='Vegetarian', choices=["Vegan", "Vegetarian", "Non-Vegetarian"])
    cuisine = StringField()
    dietType = ListField(StringField(), default=['No Data Available'])
    idealMedCond = ListField(StringField())
    avoidableMedCond = ListField(StringField())
    course = BaseField(default='Snack', choices=["Breakfast", "Lunch", "Dinner", "Snack", "Soup", "Juice"])
    calories = IntField(default=0)
    nutritionInfo = StringField()
    ingredients = StringField()
    directions = StringField()
    photoURL = StringField()
