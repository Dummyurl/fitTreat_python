'''
Created on 18-Dec-2018

@author= Balkrishna.Meena
'''
from flask_mongoengine import Document
from mongoengine.fields import StringField, ReferenceField
from mongoengine.fields import ListField
from app.models.medicines import Medicines


class Symptoms(Document):
    name = StringField(required=True, unique=True)
    indications = StringField()
    medicines = ListField(ReferenceField(Medicines))
