'''
Created on 19-Dec-2018

@author: Balkrishna.Meena
'''
import json
from typing import Any, Union

import bson
from flask import request
from flask.json import jsonify

from app.models.user import User, Messages
from attrdict import AttrDict
from mongoengine import DoesNotExist
import mongoengine

def register():
    data = AttrDict(request.get_json())
    try:
        user = User.objects(email=data.email).get()
        obj: Any = {}
        obj['error'] = "Email already in use"
        return jsonify(obj)
    except DoesNotExist:
        msg_content: str = "Dear " + data.firstName + ", <br><br> Welcome to FitTreat.<br><br> Team FitTreat";
        user = User(
            firstName=data.firstName,
            lastName=data.lastName,
            email=data.email,
            gender=data.gender,
            password=data.password,
            dateOfBirth=data.dateOfBirth,
            age=data.age,
            weight=data.weight,
            weightUnit=data.weightUnit,
            height=data.height,
            heightUnit=data.heightUnit,
            foodPreference=data.foodPreference,
            timeZone=data.timeZone,
            medicalCondition=data.medicalCondition,
            messages = [Messages(subject="Welcome", content=msg_content)]
        )
        user = user.save()
        return jsonify(user)


def activeUser(id):
    try:
        user = User.objects.get(id=bson.objectid.ObjectId(str(id)))
        json_resp = jsonify(user)
        user['mealAssigned'] = None
        unreadMsg = [msg for msg in user['messages'] if msg['readFlag'] == False]
        user['unreadCount'] = len(unreadMsg)
        return json_resp
    except DoesNotExist as e:
        return 'Some error occurred : ' + str(e)

