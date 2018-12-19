from cfenv import AppEnv

env = AppEnv()

print(env)
print(env.__dict__)
print(dir(env))

class Config(object): 
    MONGODB_SETTINGS = {
        'db': 'fitdb',
        'host': 'mongodb://conusr:Welcome1@ds113454.mlab.com/fitdb',
        'port': 13454
        # 'host': '127.0.0.1',
        # 'port': 27017,
        # 'username': '',
        # 'password': ''
    }
