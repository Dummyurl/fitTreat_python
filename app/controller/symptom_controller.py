from attrdict import AttrDict
from flask import request
from flask.json import jsonify
from flask_api import status
from mongoengine.errors import NotUniqueError, DoesNotExist

from app.models.medicines import Medicine
from app.models.symptoms import Symptom

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
            symptom = None
            try:
                symptom = Symptom.objects(name=symp['symptom']['name'])
            except DoesNotExist:
                symptom = Symptom(name=symp['symptom']['name'], medicines=medArr,
                                  indications=symp['indications'] if 'indications' in symp else None)
                try:
                    symptom.save()
                except Exception as e:
                    return jsonify({'Error': format(e)}), status.HTTP_500_INTERNAL_SERVER_ERROR
        except Exception as e:
            print(e)
            return jsonify({'Error': format(e)}), status.HTTP_500_INTERNAL_SERVER_ERROR
    return jsonify({'status': 'Data inserted successfully'}), 200


''' Initial Symptoms'''


def first5Symptoms():
    return jsonify(Symptom.objects[:5]), status.HTTP_200_OK


''' Search Symptom'''


def searchSymptom(searchParam):
    return jsonify(Symptom.objects(name__icontains=searchParam)), status.HTTP_200_OK


''' Get all symptoms'''


def getAllSymptoms():
    return jsonify(Symptom.objects), status.HTTP_200_OK


''' Delete symptoms '''


def deleteSymptoms():
    idArr = request.get_json()
    try:
        delSymps = Symptom.objects(id__in=idArr)
        if delSymps:
            delSymps = delSymps.delete()
            return jsonify(delSymps), status.HTTP_200_OK
        else:
            return jsonify({'stat': 'Symptoms not deleted'}), status.HTTP_400_BAD_REQUEST
    except Exception as e:
        return jsonify({'stat': 'Unable to delete symptoms - {}'.format(e)}), status.HTTP_500_INTERNAL_SERVER_ERROR


def addNewSymptom():
    data = AttrDict(request.get_json())

    try:
        newSymp = Symptom(name=data.name, indications=data.indications,
                          medicines=[med for med in data.medicines]).save()

        return jsonify(newSymp)
    except NotUniqueError:
        return jsonify({'status': 'Symptom already exists.'}), status.HTTP_200_OK
    except Exception as e:
        return jsonify({'status': 'Error while saving symptom'}), status.HTTP_500_INTERNAL_SERVER_ERROR
