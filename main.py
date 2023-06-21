from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():

    return "home"

if __name__ == '__main__':
                        