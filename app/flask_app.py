# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from pymongo.database import Database
from bson import ObjectId
from bson.json_util import dumps, loads 


# from flask_pymongo import PyMongo

app = Flask(__name__)

global db
db = None #type: Database

# app.config['MONGO_DBNAME'] = 'restdb'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

# mongo = PyMongo(app)

@app.route('/coffee-machines', methods=['GET'])
def get_coffee_machines():
  coffee_machines = db.products.find({"type": "COFFEE_MACHINE"})
  output = []
  def process_value(key, val):
    # if val is str or val is bool:
    #     return val
    if key == "_id":
        return str(val)
    return val

  for c in coffee_machines:
    output.append( {k: process_value(k, v) for k, v in c.items() })

  return jsonify({'result' : output})

def run(target_database: Database, **kwargs):
    global db 
    db = target_database
    app.run(**kwargs)

if __name__ == '__main__':
    app.run(debug=True)


