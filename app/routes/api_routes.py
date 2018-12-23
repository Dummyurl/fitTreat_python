from flask import render_template, redirect, url_for, jsonify, request
from app import app
from app.controller import user_controller, appData_controller, symptom_controller


@app.route('/api/loggedInUser/<id>')
def loggedInUser(id):
    return user_controller.activeUser(id)


@app.route('/api/changePassword/<email>')
def changePassword(email):
    pass


@app.route('/api/passwordResetRedirect')
def passwordResetRedirect():
    pass


@app.route('/api/resetPassword', methods=['POST'])
def resetPassword():
    pass


@app.route('/api/readMessage/<docId>/<msgId>')
def readMessage(docId, msgId):
    pass


@app.route('/api/targetWeight', methods=['PUT'])
def targetWeight():
    pass


@app.route('/api/reloadMessages/<id>')
def reloadMessages(id):
    pass


@app.route('/api/updateProfile', methods=['PUT'])
def updateProfile():
    pass


@app.route('/api/photoUpdate', methods=['POST'])
def photoUpdate():
    pass


@app.route('/api/getMeals/<userId>')
def getMeals(userId):
    pass


@app.route('/api/filterMeals/<type>/<foodPref>/<userId>')
def filterMeals(type, foodPref, userId):
    pass


@app.route('/api/initialSymptoms')
def initialSymptoms():
    return symptom_controller.first5Symptoms() #done


@app.route('/api/searchSymptoms/<searchParam>')
def searchSymptoms(searchParam):
    return symptom_controller.searchSymptom(searchParam=searchParam) #done


@app.route('/api/getAppData')
def getAppData():
    return appData_controller.getAppDefaultData() #done


@app.route('/api/sendMsgToAdmin', methods=['POST'])
def sendMsgToAdmin():
    pass
