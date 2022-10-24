# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def create_user():
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

def create():
    print("hey")