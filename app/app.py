from pymongo import MongoClient
from app.migrations.seed_skus import SeedSkus 

client = MongoClient('localhost',27017,
    username='root',
    password='example',
    authSource='admin')

db = client.db

SeedSkus().seedSkus(db)