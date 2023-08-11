from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


#$ env FLASK_APP=hello.py flask run
# * Serving Flask app "hello"
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

if __name__ == "__main__":
    app.run()
