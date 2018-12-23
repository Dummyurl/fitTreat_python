from flask import render_template, redirect, url_for, jsonify, request
from app import app
from app.controller import appData_controller, user_controller, meal_controller, medicine_controller, symptom_controller

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
    pass


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
    pass


@app.route('/admin/clearDB')
def clearDB():
    pass
