import random

from flask import Flask, send_file

import database
import models


app = Flask(__name__, static_url_path='/static')


def recommend_restaurant():
    # To start with just recommend a restaurant at random
    random_index = random.randrange(0, database.db_session.query(models.Restaurant).count())
    return database.db_session.query(models.Restaurant)[random_index]


@app.route('/')
def index():
    return send_file("templates/index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
