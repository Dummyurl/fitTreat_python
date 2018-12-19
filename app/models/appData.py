'''
Created on 18-Dec-2018

@author: Balkrishna.Meena
'''
from flask_mongoengine import Document
from mongoengine.fields import StringField

class AppData(Document):
    aboutSection=StringField()
    references=StringField()
