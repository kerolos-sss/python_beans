# mongo.py
import enum
from flask import Flask
from flask import jsonify
from flask import request
from pymongo.database import Database
from bson import ObjectId
from bson.json_util import dumps, loads 
from schema import Schema, And, Use, Optional

# from flask_pymongo import PyMongo

app = Flask(__name__)

global db
db = None #type: Database

# app.config['MONGO_DBNAME'] = 'restdb'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

# mongo = PyMongo(app)

class BasicTypes(enum.Enum):
  COFFEE_MACHINE = "COFFEE_MACHINE"
  COFFEE_POD = "COFFEE_POD"

# just to figure out how it works
# for weekday in (BasicTypes):
#    print(weekday)
#    print(weekday.value)

@app.route('/test', methods=['GET'])
def test():
  condition = {"type": "COFFEE_MACHINE"}
  output = _get_matching_products(condition)
  return jsonify({'results' : output})


@app.route('/coffee-machines', methods=['POST'])
def filter_coffee_machines():
  input_json = request.json
  schema = Schema({
    ## seems there is a adjustment needed to the error messages 
    ## TODO: I can't worry about that now
    Optional('product_type'): And(str, lambda x : x in [
      'COFFEE_MACHINE_SMALL',
      'COFFEE_MACHINE_LARGE',
      'ESPRESSO_MACHINE'
    ]),
    Optional('water_line_compatible'):  And(bool),
    # Optional('model'): And(str, lambda s: s in ['premium', ...] )
  });
  schema.validate(input_json)


  condition = {}
  condition.update(input_json)
  condition.update({"type": "COFFEE_MACHINE"})
  
  output = _get_matching_products(condition)

  return jsonify({'results' : output})



@app.route('/coffee-pods', methods=['POST'])
def filter_coffee_pods():
  input_json = request.json
  schema = Schema({
    ## seems there is a adjustment needed to the error messages 
    ## TODO: I can't worry about that now
    Optional('product_type'): And(str, lambda x : x in [
      'COFFEE_POD_SMALL',
      'COFFEE_POD_LARGE',
      'ESPRESSO_POD'
    ]),
    ## TODO: include other attributes' constraints
    Optional('pack_size'): And(str, len),
    Optional('coffee_flavor'): And(str, len),
  });
  schema.validate(input_json)


  condition = {}
  condition.update(input_json)
  condition.update({"type": "COFFEE_POD"})
  
  output = _get_matching_products(condition)

  return jsonify({'results' : output})


def _get_matching_products(condition):
  coffee_machines = db.products.find(condition)
  output = []
  def process_value(key, val):
    # if val is str or val is bool:
    #     return val
    if key == "_id":
        return str(val)
    return val

  for c in coffee_machines:
    output.append( {k: process_value(k, v) for k, v in c.items() })

  return output

def run(target_database: Database, **kwargs):
    global db 
    db = target_database
    app.run(**kwargs)

if __name__ == '__main__':
    app.run(debug=True)


