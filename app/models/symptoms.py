'''
Created on 18-Dec-2018

@author= Balkrishna.Meena
'''
from flask_mongoengine import Document
from mongoengine.fields import StringField, ReferenceField
from models.medicines import Medicine

class Symptom(Document):
    name= StringField(required=True)
    indications=StringField()
    medicines=ReferenceField(Medicine)
    