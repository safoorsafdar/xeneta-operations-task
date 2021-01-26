import os


DB = {
    "name": os.environ['POSTGRES_DB'],
    "user": os.environ['POSTGRES_USER'],
    "host": os.environ['POSTGRES_HOST'],
    "password": os.environ['POSTGRES_PASSWORD'],
    "port": os.environ['POSTGRES_PORT']
}

print(os.environ['POSTGRES_HOST'])