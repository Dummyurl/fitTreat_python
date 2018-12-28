'''
Created on 19-Dec-2018

@author: Balkrishna.Meena
'''

import bson
from flask import request, render_template
from flask.json import jsonify
from app import app
from app.models.user import User, Messages
from attrdict import AttrDict
from datetime import datetime, timedelta
from mongoengine import DoesNotExist
from cryptography.fernet import Fernet
from config import Config

import smtplib
from email.mime.text import MIMEText

'''    /*** New Registration ***/ '''


def register():
    data = AttrDict(request.get_json())
    try:
        user = User.objects(email=data.email).get()
        obj = {
            'error': "Email already in use"
        }
        return jsonify(obj)
    except DoesNotExist:
        msg_content = "Dear " + data.firstName + ", <br><br> Welcome to FitTreat.<br><br> Team FitTreat"
        user = User(
            firstName=data.firstName,
            lastName=data.lastName,
            email=data.email,
            gender=data.gender,
            password=data.password,
            dateOfBirth=data.dateOfBirth,
            age=data.age if data.age else 0,
            weight=data.weight,
            weightUnit=data.weightUnit,
            height=data.height,
            heightUnit=data.heightUnit,
            foodPreference=data.foodPreference,
            timeZone=data.timeZone,
            medicalCondition=data.medicalCondition,
            messages=[Messages(subject="Welcome", content=msg_content)]
        )
        user = user.save()
        user['password'] = None
        unreadMsg = [msg for msg in user['messages'] if msg['readFlag'] is False]
        user['unreadCount'] = len(unreadMsg)
        return jsonify(user)


''' /*** Returns Active User Details ***/ '''


def activeUser(user_id):
    try:
        user = User.objects.get(id=bson.objectid.ObjectId(str(user_id)))
        user['password'] = None
        user['mealAssigned'] = None
        unreadMsg = [msg for msg in user['messages'] if msg['readFlag'] is False]
        user['unreadCount'] = len(unreadMsg)
        json_resp = jsonify(user)
        return json_resp
    except DoesNotExist as e:
        return 'Some error occurred : ' + str(e)


''' /*** Updates message read/unread status ***/ '''


def messageReadStatusChange(user_id, msg_id):
    try:
        user = User.objects.get(id=bson.objectid.ObjectId(str(user_id)))
        # message = [msg for msg in user['messages']]
        for msg in user['messages']:
            if str(msg['_id']) == msg_id:
                print('Message Found')
                msg['readFlag'] = not (msg['readFlag'])
                try:
                    msg.save()
                    return jsonify(msg)
                except Exception as e:
                    print(e)
                    return 'Error in saving message status'
    except Exception as e:
        return 'Some error occurred : ' + str(e)


def updateGoalWeight():
    body = AttrDict(request.get_json())
    try:
        User.objects(id=body.id).update_one(targetWeight=body.targetWeight, \
            targetDate=body.targetDate, targetCalories=body.targetCalories, \
            weightUnit=body.weightUnit)

        return jsonify({'msg': 'success'})
    except DoesNotExist:
        return 'No such user found', 500


def reloadMessages(id):
    try:
        user = User.objects(id=id).get()

        return jsonify({
            'msgSummary': user.unreadCount,
            'messages': user.messages
        })
    except DoesNotExist:
        return 'No such user found', 400


def updateProfile():
    body = AttrDict(request.get_json())

    User.objects(id=body.id).update_one(\
        weight = body.weight,
        weightUnit = body.weightUnit,
        height = body.height,
        heightUnit = body.heightUnit,
        foodPreference = body.foodPreference,
        medicalCondition = body.medicalCondition,
        firstName = body.firstName,
        lastName = body.lastName
    )

    return activeUser(body.id)

def userPhotoUpdate():
    body = AttrDict(request.get_json())

    try:
        upd = User.objects(id=body.id).update_one(userPhoto=body.userPhoto)
        if upd:
            return jsonify({ 'id':body.id, 'photoString':body.userPhoto })
        else:
            return 'Cannot update profile photo', 500
    except DoesNotExist:
        return 'No such user found', 400

def changePassword(email):
    try:
        user = User.objects(email=email).get()
        print(user)

        userId = user.id
        fern = Fernet(Config.crptrKey)
        resetToken = fern.encrypt('{}r353tT0k3n'.format(userId).encode()).decode('utf-8')
        resetExpiryTime = datetime.now() + timedelta(minutes=30)
        
        User.objects(id=userId)\
            .update_one(resetPasswordToken=resetToken, resetPasswordExpires=resetExpiryTime)
        
        userName = user.firstName
        link = "http://localhost:8888/api/passwordResetRedirect?token=" + resetToken + "&id=" + str(userId)

        #return render_template('changePassword.html', username=userName, link=link)

        msg = MIMEText(render_template('changePassword.html', username=userName, link=link), 'html')
        msg['Subject'] = 'FitTreat : Password Reset'
        msg['From'] = 'FitTreat app116066240@heroku.com'
        msg['To'] = email

        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.login('consult.saurabh@gmail.com', 'Welcome$000')
            s.sendmail('consult.saurabh@gmail.com', [email], msg.as_string())
            s.close()
            print('mail sent')
            return {'msg': 'Please check your registered email'}, 200
        except Exception as e:
            print('error while sending mail')
            print(e)
            return {'msg': 'Some error occurred.'}, 400
    except DoesNotExist:
        return 'No user found with email - {}'.format(email), 404


def resetPassword():
    try:
        body = AttrDict(request.get_json())
        
        token = body.token
        dob = body.dob
        password = body.password

        fern = Fernet(Config.crptrKey)
        decryptToken = fern.decrypt(token.encode()).decode()
        
        userId = decryptToken[0:decryptToken.index("r353tT0k3n")]

        print(userId)

        try:
            user = User.objects(id=userId).get()

            if datetime.now() < user.resetPasswordExpires:
                if user.dateOfBirth == dob:
                    User.objects(id=userId).update_one(password=password, resetPasswordExpires=datetime.now())
                    return app.send_static_file('passwordReset/passwordChangeSuccess.html')
                else:
                    return jsonify({'msg': 'DOB did not match'}), 500
            else:
                return app.send_static_file('passwordReset/passwordLinkExpired.html')
            
        except DoesNotExist:
            return 'No such user found', 400
    except Exception as e:
        print(e)
        return 'Something wrong happened', 500