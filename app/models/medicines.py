'''
Created on 18-Dec-2018

@author= Balkrishna.Meena
'''
from flask_mongoengine import Document
from mongoengine.fields import StringField
from djangotoolbox.fields import ListField
class Medicine(Document):
    name=StringField()
    dosage=StringField()
    instructions=StringField()
    ingredients=ListField(StringField())