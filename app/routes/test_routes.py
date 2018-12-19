from flask import render_template, redirect, url_for, jsonify, request
from app.models.user import User
from app import app


@app.errorhandler(404)
def handleError404(e):
    print(e)
    return 'Oops. Looks like you have entered a wrong link. Please check the link and try again.'


@app.errorhandler(500)
def handleError500(e):
    print(e)
    return 'Oops. Something went wrong. Please try again. If problem persists please contact system administrator.'


@app.errorhandler(403)
def handleError403(e):
    print(e)
    return 'Oops. You are not allowed to access this URL. Please check with system administrator.'


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/home')
def home():
    user = {'username': 'Saurabh'}
    return render_template('home.html', title='Home', user=user)


@app.route('/addUser/<email>/<fname>/<lname>', methods=['POST', 'GET'])
def addUser(email, fname, lname):
    mu = User(email=email, firstName=fname, lastName=lname)
    mu.save()

    return 'MUser saved. Check DB'


@app.route('/getUser/<email>')
def getUser(email):
    users = User.objects(email=email)
    
    print(users)

    if users:
        response = jsonify(users[0])
        return response

    return 'No such user found', 404


@app.route('/getUsers')
def getUsers():
    users = User.objects

    print(users)
    response = jsonify(users)
    return response


@app.route('/updateUser/<email>/<fname>/<lname>')
def updateUser(email, fname, lname):
    r = User.objects(email=email).update_one(firstName=fname, lastName=lname)
    print(r)

    return 'User updated. Check DB'


@app.route('/deleteUser/<email>')
def deleteUser(email):
    dd = User.objects(email=email).delete()
    print(dd)

    if dd:
        return 'User deleted'

    return 'User not deleted'


@app.route('/postdata', methods=['POST'])
def postData():
    print('data')
    print(request.data)

    print('args')
    print(request.args)

    print('files')
    print(request.files)

    print('form')
    print(request.form)

    print('values')
    print(request.values)

    print('json')
    print(request.get_json())

    return 'Done'