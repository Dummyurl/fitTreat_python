from flask import render_template, redirect, url_for, jsonify, request
from app import app


@app.route('/admin/editAppData/<id>', methods=['PUT'])
def editAppData(id):
    pass


@app.route('/admin/addMeals', methods=['POST'])
def addMeals():
    pass


@app.route('/admin/addNewMeal', methods=['POST'])
def addNewMeal():
    pass


@app.route('/admin/updateMeal/<id>', methods=['PUT'])
def updateMeal(id):
    pass


@app.route('/admin/deleteMeal/<id>', methods=['DELETE'])
def deleteMeal(id):
    pass


@app.route('/admin/getMealsList')
def getMealsList():
    pass


@app.route('/admin/addMedicines', methods=['POST'])
def addMedicines():
    pass


@app.route('/admin/addNewMedicine', methods=['POST'])
def addNewMedicine():
    pass


@app.route('/admin/getAllMeds')
def getAllMeds():
    pass


@app.route('/admin/deleteMeds', methods=['POST'])
def deleteMeds():
    pass


@app.route('/admin/addSymptoms', methods=['POST'])
def addSymptoms():
    pass


@app.route('/admin/addNewSymptom', methods=['POST'])
def addNewSymptom():
    pass


@app.route('/admin/getAllSymptoms')
def getAllSymptoms():
    pass


@app.route('/admin/deleteSymptopms', methods=['POST'])
def deleteSymptopms():
    pass


@app.route('/admin/dbStats')
def dbStats():
    pass


@app.route('/admin/templateDownload/<name>')
def templateDownload(name):
    pass


@app.route('/admin/deleteCollection/<name>', methods=['DELETE'])
def deleteCollection(name):
    pass


@app.route('/admin/clearDB')
def clearDB():
    pass
