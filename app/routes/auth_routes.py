from flask import render_template, redirect, url_for, jsonify, request
from app import app
from app.controller import user_controller
import flask_bcrypt
import bcrypt
import dateutil

@app.route('/auth/test')
def test():
    str = 'Balkrishna'
    generated = flask_bcrypt.generate_password_hash(str,5)
    print(generated)
    if flask_bcrypt.check_password_hash(generated,'Balkrishna1'):
         return 'Password Match'
    else:
         return 'Password Mis-match'


''' /*** User Registration ***/ '''


@app.route('/auth/register', methods=['POST'])
def register():
    return user_controller.register()


@app.route('/auth/login', methods=['POST'])
def login():
    pass
