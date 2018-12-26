'''
Created on 19-Dec-2018

@author: Balkrishna.Meena
'''

import bson
from flask import request
from flask.json import jsonify
from app.models.user import User, Messages
from attrdict import AttrDict
from mongoengine import DoesNotExist


'''    /*** New Registration ***/ '''


def register():
    data = AttrDict(request.get_json())
    try:
        user = User.objects(email=data.email).get()
        obj = {
            'error': "Email already in use"
        }
        return jsonify(obj)
    except DoesNotExist:
        msg_content = "Dear " + data.firstName + ", <br><br> Welcome to FitTreat.<br><br> Team FitTreat"
        user = User(
            firstName=data.firstName,
            lastName=data.lastName,
            email=data.email,
            gender=data.gender,
            password=data.password,
            dateOfBirth=data.dateOfBirth,
            age=data.age if data.age else 0,
            weight=data.weight,
            weightUnit=data.weightUnit,
            height=data.height,
            heightUnit=data.heightUnit,
            foodPreference=data.foodPreference,
            timeZone=data.timeZone,
            medicalCondition=data.medicalCondition,
            messages=[Messages(subject="Welcome", content=msg_content)]
        )
        user = user.save()
        user['password'] = None
        unreadMsg = [msg for msg in user['messages'] if msg['readFlag'] is False]
        user['unreadCount'] = len(unreadMsg)
        return jsonify(user)


''' /*** Returns Active User Details ***/ '''


def activeUser(user_id):
    try:
        user = User.objects.get(id=bson.objectid.ObjectId(str(user_id)))
        user['password'] = None
        user['mealAssigned'] = None
        unreadMsg = [msg for msg in user['messages'] if msg['readFlag'] is False]
        user['unreadCount'] = len(unreadMsg)
        json_resp = jsonify(user)
        return json_resp
    except DoesNotExist as e:
        return 'Some error occurred : ' + str(e)


''' /*** Updates message read/unread status ***/ '''


def messageReadStatusChange(user_id,msg_id):
    try:
        user = User.objects.get(id=bson.objectid.ObjectId(str(user_id)))
        # message = [msg for msg in user['messages']]
        for msg in user['messages']:
            if(str(msg['_id']) == msg_id):
                print('Message Found')
                msg['readFlag'] =  not (msg['readFlag'])
                try:
                    msg.save()
                    return jsonify(msg)
                except Exception as e:
                    print(e)
                    return 'Error in saving message status'
    except Exception as e:
        return 'Some error occurred : ' + str(e)
