'''
Created on 19-Dec-2018

@author: Balkrishna.Meena
'''
import json

from flask import request
from app.models.user import User
from attrdict import AttrDict


def register():
    # email = request.data['email']
    try:
        data = AttrDict(request.get_json())
        user = User(
            firstName = data.firstName,
            lastName =  data.lastName,
            email = data.email,
            gender = data.gender,
            password = data.password,
            dateOfBirth =  data.dateOfBirth,
            age = data.age,
            weight = data.weight,
            weightUnit = data.weightUnit,
            height = data.height,
            heightUnit =  data.heightUnit,
            foodPreference = data.foodPreference,
            timeZone =  data.timeZone,
            medicalCondition = data.medicalCondition
        )
        user.save()
        print('Data Saved')
    except Exception as e: 
        print('Data Save Error')
        print(e)
        return 'Error Occurred'
    return 'User Created'
    