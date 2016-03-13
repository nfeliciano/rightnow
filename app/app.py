import random

from nocache import nocache
from flask import Flask, send_file, jsonify, request
import database
import models
from json import dumps
from sqlalchemy.orm import class_mapper

def serialize(model):
  """Transforms a model into a dictionary which can be dumped to JSON."""
  # first we get the names of all the columns on your model
  columns = [c.key for c in class_mapper(model.__class__).columns]
  # then we return their values in a dict
  return dict((c, getattr(model, c)) for c in columns)


app = Flask(__name__, static_url_path='/static')


def random_in(model=models.Restaurant):
    # To start with just recommend a restaurant at random
    random_index = random.randrange(0, database.db_session.query(model).count())
    return database.db_session.query(model)[random_index]



@app.route('/api')
@nocache
def api_request():
    try:
        data = list()
        random = request.args.get('random')
        table = request.args.get('table')
        model_table = None
        if(table):
            model_table = {
                'restaurants' : models.Restaurant,
                'activities' : models.Activity,
                'events' : models.Event
            }[table]

        if(random and random.isdigit()):
            for i in range(int(random)):
                pass
                data.append(serialize(random_in(model_table)))
        elif(True):
            pass
        result = {'result' : data};
        return jsonify(**result)#jsonify(**serialize(recommend_restaurant()))
    except:
        return jsonify(**dict({"error_id":100, "error_message":"Not sure what went wrong :'(","error_name":"unspecified_error"}))

@app.route('/login', methods=['GET', 'POST'])
@nocache
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username)
    print(password)
    return ''

@app.route('/')
@nocache
def index():
    return send_file("templates/index.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
