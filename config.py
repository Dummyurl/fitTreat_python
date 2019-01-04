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
    userId = os.getenv("SENDGRID_USERNAME")
    password = os.getenv("SENDGRID_PASSWORD")
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT")
    # uri = env.uris[0] or 'localhost:8888'
    uri = os.getenv("uri") or 'localhost:8888'
    dbName = 'fit_treat'
    MONGODB_SETTINGS = {
        'db': dbName,
        'host': 'mongodb://fitTreat:Welcome12#@ds119343.mlab.com:19343/' + dbName,
    }
