'''
Created on 18-Dec-2018

@author: Balkrishna.Meena
'''
from flask_mongoengine import Document
from mongoengine.fields import StringField, EmailField, DateTimeField, IntField
from mongoengine.base.fields import BaseField
from datetime import datetime

class User(Document):
    firstName = StringField(required=True)
    lastName = StringField(required=True,default='')
    email = EmailField(required=True)
    '''
    gender = BaseField(required=True,default='Male',choices=['Male','Female','Other'])
    password = StringField(required=True)
    resetPasswordToken = StringField()
    resetPasswordExpires = DateTimeField()
    role = BaseField(default='User',choices=['User','Admin'])
    dateOfBirth = StringField(required=True) # YYYY/MM/DD Format
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
    targetDate = StringField(default='') # YYYY/MM/DD format
    targetCalories = IntField(default=0)
    accountCreationDate = DateTimeField(default=datetime.now)
    
    userPhoto = {
        type:String,
        default:""
    },
    messages:[MessageSchema],
    mealAssigned:[{type:Schema.Types.ObjectId,ref:'meal'}],
    mealExpiry:{
        type:Number,
        default:0
    }'''
