'''
Created on 18-Dec-2018

@author: Balkrishna.Meena
'''
from datetime import datetime
import flask_bcrypt
from mongoengine.signals import pre_save
from dateutil import parser, relativedelta
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
    createDate = DateTimeField(default=datetime.now)
    readFlag = BooleanField(default=False)
    content = StringField()
    _id = ObjectIdField(default=ObjectId)


class User(Document):
    firstName = StringField(required=True)
    lastName = StringField(required=True, default='')
    email = EmailField(required=True)
    gender = BaseField(required=True, default='Male', choices=['Male', 'Female', 'Other'])
    password = StringField(required=True)
    resetPasswordToken = StringField()
    resetPasswordExpires = DateTimeField()
    role = BaseField(default='User', choices=['User', 'Admin'])
    dateOfBirth = StringField(required=True)  # YYYY/MM/DD Format
    age = IntField(required=True, default=0)
    weight = IntField(required=True, default=0)
    weightUnit = BaseField(required=True, default='kg', choices=['kg', 'lb'])
    height = IntField(required=True, default=0)
    heightUnit = BaseField(required=True, default='cm', choices=['cm', 'm', 'ft'])
    foodPreference = BaseField(required=True, default='Vegetarian', choices=['Vegan', 'Vegetarian', 'Non-Vegetarian'])
    timeZone = StringField(default='0')  # Timezone Offset Value
    bmi = IntField(default=0)
    medicalCondition = StringField()
    targetWeight = IntField(default=0)
    targetDate = StringField(default='')  # YYYY/MM/DD format
    targetCalories = IntField(default=0)
    accountCreationDate = DateTimeField(default=datetime.now)
    userPhoto = StringField()
    messages = ListField(EmbeddedDocumentField(Messages))
    mealAssigned = ListField(ReferenceField(Meal))
    mealExpiry = DateTimeField()
    unreadCount = IntField(default=0)

    @staticmethod
    def pre_save_func(sender, document):
        document['password'] = str(flask_bcrypt.generate_password_hash(document['password']).decode('utf-8'))
        dob = parser.parse(document['dateOfBirth'])
        today = datetime.today()
        age = relativedelta.relativedelta(today, dob)
        document['age'] = age.years


pre_save.connect(User.pre_save_func, sender=User)
