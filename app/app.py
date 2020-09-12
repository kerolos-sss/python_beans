from pymongo import MongoClient
from app.migrations.seed_skus import SeedSkus 
from app import flask_app 

client = MongoClient('localhost',27017,
    username='root',
    password='example',
    authSource='admin')

db = client.db

SeedSkus().seedSkus(db)

def run():
    flask_app.run(db, debug=True)
    
if __name__ == "__main__":
    flask_app.run(db, debug=True)