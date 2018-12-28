from flask import render_template, redirect, url_for, jsonify, request
from app import app
from app.controller import user_controller, appData_controller, symptom_controller
from app.models.user import User
from mongoengine import DoesNotExist
from datetime import datetime, timedelta

''' /*** Pull Active User Details ***/ ''' #done
@app.route('/api/loggedInUser/<user_id>')
def loggedInUser(user_id):
    return user_controller.activeUser(user_id)


''' /*** Send password change email to user ***/ ''' #done
@app.route('/api/changePassword/<email>')
def changePassword(email):
    return user_controller.changePassword(email) 


''' /*** Show password change view ***/ ''' #done
@app.route('/api/passwordResetRedirect') 
def passwordResetRedirect():
    token = request.args.get('token')
    id = request.args.get('id')

    if id and token:
        try:
            user = User.objects(id=id).get()

            print('user.id', user.id)
            print('userId', id)
            print('token', token)
            print('resetPasswordToken', user.resetPasswordToken)

            if str(user.id) == id and user.resetPasswordToken == token:
                if datetime.now() < user.resetPasswordExpires:
                    resp = app.send_static_file('passwordReset/passwordReset.html')
                    resp.set_cookie('token', value=user.resetPasswordToken, expires=datetime.now() + timedelta(minutes=5))
                    return resp
                else:
                    return app.send_static_file('passwordReset/passwordLinkExpired.html')
            else:
                print('invalid token')
                return 'Invalid token', 500
        except DoesNotExist:
            print('no such user found')
            return 'No such user found', 400
    else:
        print('od or token not found')
        return 'Id or token not found', 400


''' /*** Reset user password ***/ ''' #done
@app.route('/api/resetPassword', methods=['POST'])
def resetPassword():
    return user_controller.resetPassword()


''' /*** Change status of message to read/unread ***/ ''' #done
@app.route('/api/readMessage/<user_id>/<msg_id>')
def readMessage(user_id, msg_id):
    return user_controller.messageReadStatusChange(user_id,msg_id)


''' /*** Update weight target ***/ ''' #done
@app.route('/api/targetWeight', methods=['PUT'])
def targetWeight():
    return user_controller.updateGoalWeight()


''' /*** Reload user messages ***/ ''' #done
@app.route('/api/reloadMessages/<id>')
def reloadMessages(id):
    return user_controller.reloadMessages(id)


''' /*** Update user profile ***/ ''' #done
@app.route('/api/updateProfile', methods=['PUT'])
def updateProfile():
    return user_controller.updateProfile()


''' /*** Update user photo ***/ ''' #done
@app.route('/api/photoUpdate', methods=['POST'])
def photoUpdate():
    return user_controller.userPhotoUpdate()


''' /*** Get meals assigned to user ***/ '''
@app.route('/api/getMeals/<userId>')
def getMeals(userId):
    pass


''' /*** Filter meals ***/ '''
@app.route('/api/filterMeals/<type>/<foodPref>/<userId>')
def filterMeals(type, foodPref, userId):
    pass


''' /* Initial Symptoms */ ''' #done
@app.route('/api/initialSymptoms')
def initialSymptoms():
    return symptom_controller.first5Symptoms()


''' /* Search Symptom */ ''' #done
@app.route('/api/searchSymptoms/<searchParam>')
def searchSymptoms(searchParam):
    return symptom_controller.searchSymptom(searchParam=searchParam)


''' /*** Get app data ***/ ''' #done
@app.route('/api/getAppData')
def getAppData():
    return appData_controller.getAppDefaultData()


''' /*** Send message to admin ***/ ''' #done
@app.route('/api/sendMsgToAdmin', methods=['POST'])
def sendMsgToAdmin():
    body = request.get_json()
    senderId = body['id']
    msg = body['msg']

    print('Admin msg sent by {}. Message: {}'.format(senderId, msg))

    return jsonify({'msg': 'Thank you for reaching out to us. Will revert asap.'})
