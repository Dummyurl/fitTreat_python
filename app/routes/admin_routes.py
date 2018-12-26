from attrdict import AttrDict
from flask import request
from flask.json import jsonify
from mongoengine import DoesNotExist, OperationError
from mongoengine.connection import _get_db, _get_connection
from app.models.user import User,Messages
from app.models.meal import Meal
from app.models.medicines import Medicine
from app.models.symptoms import Symptom
import bson
from app import app, mdb
from app.controller import appData_controller, meal_controller, medicine_controller, symptom_controller


@app.route('/admin/editAppData/<id>', methods=['PUT'])
def editAppData(id):
    return appData_controller.setAppDefaultData(id) #done


@app.route('/admin/addMeals', methods=['POST'])
def addMeals():
    return meal_controller.addMealData()


@app.route('/admin/addNewMeal', methods=['POST'])
def addNewMeal():
    return meal_controller.addNewMeal() #done


@app.route('/admin/updateMeal/<id>', methods=['PUT'])
def updateMeal(id):
    return meal_controller.updateMeal(id) #done


@app.route('/admin/deleteMeal/<id>', methods=['DELETE'])
def deleteMeal(id):
    return meal_controller.deleteMeal(id) #done


@app.route('/admin/getMealsList')
def getMealsList():
    return meal_controller.getMealsList() #done


@app.route('/admin/addMedicines', methods=['POST'])
def addMedicines():
    return medicine_controller.addMedicines() #done


@app.route('/admin/addNewMedicine', methods=['POST'])
def addNewMedicine():
    return medicine_controller.addNewMedicine() #done


@app.route('/admin/getAllMeds')
def getAllMeds():
    return medicine_controller.getAllMedicines() #done


@app.route('/admin/deleteMeds', methods=['POST'])
def deleteMeds():
    return medicine_controller.deleteMeds() #done


@app.route('/admin/addSymptoms', methods=['POST'])
def addSymptoms():
    return symptom_controller.addMedicineData()


@app.route('/admin/addNewSymptom', methods=['POST'])
def addNewSymptom():
    return symptom_controller.addNewSymptom() #done


@app.route('/admin/getAllSymptoms')
def getAllSymptoms():
    return symptom_controller.getAllSymptoms() #done


@app.route('/admin/deleteSymptopms', methods=['POST'])
def deleteSymptopms():
    return symptom_controller.deleteSymptoms() #done


@app.route('/admin/dbStats')
def dbStats():
    obj = {
        'users': User.objects.count(),
        'meals': Meal.objects.count(),
        'medicines': Medicine.objects.count(),
        'symptoms': Symptom.objects.count()
    }

    return jsonify(obj), 200


@app.route('/admin/templateDownload/<name>')
def templateDownload(name):
    filePath = {
        'meal':'mealData.xlsx',
        'medicine':'medicineData.json',
        'symptoms':'SymptomsData.json'
    }

    return app.send_static_file(filePath[name]) #done


@app.route('/admin/deleteCollection/<name>', methods=['DELETE'])
def deleteCollection(name):
    if(name == 'users'):
        print('Dropping user collection')
        User.drop_collection()
    elif(name == 'meals'):
        print('Dropping meal collection')
        Meal.drop_collection()
    elif(name == 'meds'):
        print('Dropping medicine collection')
        Medicine.drop_collection()
    elif(name == 'symptoms'):
        print('Dropping symptom collection')
        Symptom.drop_collection()
    else:
        print('Wrong collection name provided: {}'.format(name))
        return 'Wrong collection name provided: {}'.format(name), 400

    return '{} collection deleted'.format(name), 200 #done



@app.route('/admin/clearDB')
def clearDB():
    db = _get_db()
    conn = _get_connection()
    conn.drop_database(db)

    return 'DB {} cleared'.format(db.name), 200 #done


''' /*** Send Message to a user ***/ '''  # done


@app.route('/admin/sendMsgToUser',methods=['POST'])
def sendMsgToUser():
    msg_data = AttrDict(request.get_json())
    user_id = msg_data.userId
    new_msg = Messages(subject=msg_data.message.subject,content=msg_data.message.content)
    try:
        user =User.objects.get(id=bson.objectid.ObjectId(str(user_id)))
        user['messages'].append(new_msg)
        user.save()
        resp = {'stat':"Message Sent Successfully"}
        return jsonify(resp), 200
    except DoesNotExist as e:
        print(e)
        return str(e), 404
    except Exception as e:
        print(e)
        return  str(e), 500

