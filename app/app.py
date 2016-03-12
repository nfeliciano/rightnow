from flask import Flask, send_file
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return send_file("templates/index.html")

if __name__ == '__main__':
    app.run()
