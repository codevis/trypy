from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hey i am shelly</h1>"

if __name__ == '__main__':
    app.run(port=5000, threaded=True)