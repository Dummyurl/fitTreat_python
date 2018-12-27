from flask import request
from flask.json import jsonify

from attrdict import AttrDict
from mongoengine import NotUniqueError

from app.models.medicines import Medicine


def addMedicines():
    data = request.get_json()
    meds = Medicine.objects.insert([Medicine(name=med['name'], dosage=med['dosage'] if 'dosage' in med else None,
                                             instructions=med['instructions'] if 'instructions' in med else None,
                                             ingredients=[ing for ing in med['ingredients']]) for med in data])
    return jsonify(meds)


def getAllMedicines():
    return jsonify(Medicine.objects)


def deleteMeds():
    idArr = request.get_json()

    try:
        delMeds = Medicine.objects(id__in=idArr)

        if delMeds:
            delMeds = delMeds.delete()
            return jsonify(delMeds)
        else:
            return 'Medicines not deleted', 400
    except Exception as e:
        return 'Unable to delete medicines - {}'.format(e)


def addNewMedicine():
    data = AttrDict(request.get_json())

    try:
        newMed = Medicine(name=data.name, dosage=data.dosage, \
                          instructions=data.instructions, ingredients=[ing for ing in data.ingredients]).save()
        return jsonify(newMed)
    except NotUniqueError:
        return 'Medicine already exists.'
    except Exception as e:
        return 'Error while saving medicine', 400
