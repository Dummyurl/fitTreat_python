from flask import render_template, redirect, url_for, jsonify, request
from app import app
from app.controller import user_controller

@app.route('/auth/test')
def test():
    pass


@app.route('/auth/register', methods=['POST'])
def register():
    return user_controller.register()


@app.route('/auth/login', methods=['POST'])
def login():
    pass
