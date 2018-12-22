'''
Created on 18-Dec-2018

@author: Balkrishna.Meena
'''
from datetime import datetime

from bson import ObjectId
from mongoengine.fields import ListField
from flask_mongoengine import Document
from mongoengine.base.fields import BaseField, ObjectIdField
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import StringField, EmailField, DateTimeField, IntField, \
    EmbeddedDocumentField, ReferenceField, BooleanField

from app.models.meal import Meal

class Messages(EmbeddedDocument):
    subject = StringField()
    createDate = DateTimeField(default = datetime.now)
    readFlag = BooleanField(default=False)
    content = StringField()
    _id = ObjectIdField(default= ObjectId)


class User(Document):
    firstName = StringField(required=True)
    lastName = StringField(required=True,default='')
    email = EmailField(required=True)
    gender = BaseField(required=True,default='Male',choices=['Male','Female','Other'])
    password = StringField(required=True)
    resetPasswordToken = StringField()
    resetPasswordExpires = DateTimeField()
    role = BaseField(default='User',choices=['User','Admin'])
    dateOfBirth = StringField(required=True)  # YYYY/MM/DD Format
    age = IntField(required=True,default=0) 
    weight = IntField(required=True,default=0) 
    weightUnit = BaseField(required=True,default='kg',choices=['kg','lb'])
    height = IntField(required=True,default=0)
    heightUnit = BaseField(required=True,default='cm',choices=['cm','m','ft'])
    foodPreference = BaseField(required=True,default='Vegetarian',choices=['Vegan','Vegetarian','Non-Vegetarian'])
    timeZone = StringField(default='UTC')
    bmi = IntField(default=0)
    medicalCondition = StringField()
    targetWeight = IntField(default=0)
    targetDate = StringField(default='')  # YYYY/MM/DD format
    targetCalories = IntField(default=0)
    accountCreationDate = DateTimeField(default=datetime.now)
    userPhoto = StringField()
    messages = ListField(EmbeddedDocumentField(Messages))
    mealAssigned = ListField(ReferenceField(Meal))
    mealExpiry = IntField(default=0)
