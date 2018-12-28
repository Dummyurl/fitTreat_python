from cfenv import AppEnv
import os

env = AppEnv()

print(env)
#print(env.__dict__)
#print(dir(env))

class Config(object): 
    #crptrKey = 'R@nd0m5tr1ngt0g3ner@t3Pa55w0rd'
    crptrKey = b'WWUV2cX5GVM5K2iFu_MauyOoecTvUNGabtpG4z8TAEY='
    port = os.getenv("PORT") or 8888
    s3URL = 'https://s3.us-east-2.amazonaws.com/fittreatstorage/meal_images_dev/'
    userId = 'app116066240@heroku.com'
    password = 'Welcome12#'
    dbName = 'fitdb'
    uri = env.uris[0] or 'localhost:8888'
    MONGODB_SETTINGS = {
        'db': dbName,
        'host': 'mongodb://conusr:Welcome1@ds113454.mlab.com/' + dbName,
        'port': 13454,
        #'host': '127.0.0.1',
        #'port': 27017,
        'username': 'conusr',
        'password': 'Welcome1'
    }
