from flask import request
from flask.json import jsonify

from attrdict import AttrDict
from mongoengine import DoesNotExist

from app.models.appData import AppData

def setAppDefaultData(id):
    data = AttrDict(request.get_json())
    print('printing data')
    print(data)

    try:
        ad = AppData.objects(id=id).update_one(aboutSection=data.aboutSection, references=data.references)
        print('printing ad')
        print(jsonify(ad))
        return jsonify({'status': 'success'})
    except Exception as e:
        print('Error while saving app data', e)
        return 'Error while saving app data', 400


def getAppDefaultData():
    return jsonify(AppData.objects.get())