from flask.json import JSONEncoder
from flask_mongoengine import BaseQuerySet
from app.models import User


class Encoder(JSONEncoder):
    def default(self, obj):
        print(type(obj))
        if isinstance(obj, User):
            return {
                'email': obj.email,
                'firstName': obj.firstName,
                'lastName': obj.lastName
            }
        elif isinstance(obj, BaseQuerySet):
            ret = []
            for o in obj:
                ret.append(self.default(o))
            return ret
        return super(Encoder, self).default(obj)
