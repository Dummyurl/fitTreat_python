from flask import render_template, redirect, url_for, jsonify, request
from app import app


@app.route('/auth/test')
def test():
    pass


@app.route('/auth/register', methods=['POST'])
def register():
    pass


@app.route('/auth/login', methods=['POST'])
def login():
    pass
