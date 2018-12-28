from flask import render_template, redirect, url_for, jsonify, request
from app import app
from app.controller import user_controller, appData_controller, symptom_controller

''' /*** Pull Active User Details ***/ ''' # done


@app.route('/api/loggedInUser/<user_id>')
def loggedInUser(user_id):
    return user_controller.activeUser(user_id)


@app.route('/api/changePassword/<email>')
def changePassword(email):
    return user_controller.changePassword(email) #done


@app.route('/api/passwordResetRedirect')
def passwordResetRedirect():
    pass


@app.route('/api/resetPassword', methods=['POST'])
def resetPassword():
    return user_controller.resetPassword() #done


''' /*** Change status of message to read/unread ***/ ''' # done


@app.route('/api/readMessage/<user_id>/<msg_id>')
def readMessage(user_id, msg_id):
    return user_controller.messageReadStatusChange(user_id,msg_id)


@app.route('/api/targetWeight', methods=['PUT'])
def targetWeight():
    return user_controller.updateGoalWeight() #done


@app.route('/api/reloadMessages/<id>')
def reloadMessages(id):
    return user_controller.reloadMessages(id) #done


@app.route('/api/updateProfile', methods=['PUT'])
def updateProfile():
    return user_controller.updateProfile() #done


@app.route('/api/photoUpdate', methods=['POST'])
def photoUpdate():
    pass


@app.route('/api/getMeals/<userId>')
def getMeals(userId):
    pass


@app.route('/api/filterMeals/<type>/<foodPref>/<userId>')
def filterMeals(type, foodPref, userId):
    pass


''' /* Initial Symptoms */ '''


@app.route('/api/initialSymptoms')
def initialSymptoms():
    return symptom_controller.first5Symptoms() #done


''' /* Search Symptom */ '''


@app.route('/api/searchSymptoms/<searchParam>')
def searchSymptoms(searchParam):
    return symptom_controller.searchSymptom(searchParam=searchParam) #done


@app.route('/api/getAppData')
def getAppData():
    return appData_controller.getAppDefaultData() #done


@app.route('/api/sendMsgToAdmin', methods=['POST'])
def sendMsgToAdmin():
    pass
