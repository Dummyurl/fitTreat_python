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
    userId = 'app116066240@heroku.com' # fitTreat Heroku Account
    smtp_host = 'smtp.sendgrid.net'
    smtp_port = 465
    password = 'Welcome12#'
    dbName = 'fit_treat'
    # uri = env.uris[0] or 'localhost:8888'
    uri = 'localhost:8888'
    MONGODB_SETTINGS = {
        'db': dbName,
        'host': 'mongodb://fitTreat:Welcome12#@ds119343.mlab.com:19343/' + dbName,
        # 'port': 27017,
    }
