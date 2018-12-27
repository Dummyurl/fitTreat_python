from flask import request
from flask.json import jsonify

from app.models.medicines import Medicine
from app.models.symptoms import Symptom

from attrdict import AttrDict
from mongoengine import NotUniqueError
from attrdict import AttrDict
from flask_api import status


'''   /* Add Symptoms in bulk*/ '''


def bulkSymptomsUpload():
    symp_data = request.get_json()
    for symp in symp_data:
        medSearchArr = []
        for med in symp['medicines']:
            medSearchArr.append(med['name'])
        try:
            medicine = Medicine.objects(name__in=medSearchArr)
            medArr = []
            for medRef in medicine:
                medArr.append(medRef)
            try:
                symptom = Symptom(name=symp['symptom']['name'], medicines=medArr,
                                  indications=symp['indications'] if 'indications' in symp else None)
                symptom.save()
            except Exception as e:
                print(e)
                return format(e), status.HTTP_500_INTERNAL_SERVER_ERROR
        except Exception as e:
            print(e)
            return 'Error Occurred : ' + format(e), status.HTTP_500_INTERNAL_SERVER_ERROR
    return jsonify({'status':'Data inserted successfully'}), 200


def first5Symptoms():
    return jsonify(Symptom.objects[:5])

def searchSymptom(searchParam):
    return jsonify(Symptom.objects(name__icontains=searchParam))

def getAllSymptoms():
    return jsonify(Symptom.objects)

def deleteSymptoms():
    idArr = request.get_json()

    try:
        delSymps = Symptom.objects(id__in=idArr)
        
        if delSymps:
            delSymps = delSymps.delete()
            return jsonify(delSymps)
        else:
            return 'Symptoms not deleted', 400
    except Exception as e:
        return 'Unable to delete symptoms - {}'.format(e)


def addNewSymptom():
    data = AttrDict(request.get_json())

    try:
        newSymp = Symptom(name=data.name, indications=data.indications, \
            medicines=[med for med in data.medicines]).save()

        return jsonify(newSymp)
    except NotUniqueError:
        return 'Symptom already exists.'
    except Exception as e:
        return 'Error while saving symptom', 400