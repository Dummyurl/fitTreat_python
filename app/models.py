from flask_mongoengine import Document
from mongoengine import StringField


class User(Document):
    email = StringField(required=True)
    firstName = StringField(required=True)
    lastName = StringField(required=True)

    def __str__(self):
        return '<MUser {}, {}, {}>'.format(self.firstName, self.lastName, self.email)
