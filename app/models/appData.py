'''
Created on 18-Dec-2018

@author: Balkrishna.Meena
'''
from flask_mongoengine import Document
from mongoengine.fields import StringField


class App_Data(Document):
    aboutSection = StringField(default='This is a test html text.')
    references = StringField(default='This is a test reference text.')
