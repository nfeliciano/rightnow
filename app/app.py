import random

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


def recommend_restaurant():
    # To start with just recommend a restaurant at random
    random_index = random.randrange(0, database.db_session.query(models.Restaurant).count())
    return database.db_session.query(models.Restaurant)[random_index]


@app.route('/api')
def api_request():
    random = request.args.get('random')
    if(random.isdigit()):
        data = list()
        for i in range(int(random)):
            data.append(serialize(recommend_restaurant()))

        result = {'result' : data};
        return jsonify(**result)

    return jsonify(**[])#jsonify(**serialize(recommend_restaurant()))

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username)
    print(password)
    return ''

@app.route('/')
def index():
    return send_file("templates/index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
