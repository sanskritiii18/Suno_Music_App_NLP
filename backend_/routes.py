from flask import Flask, jsonify, request
from flask_cors import CORS
from backend_.auth import login_user, register_user

server = Flask(__name__)
CORS(server)

@server.route("/login",methods=["POST"])
def login():
    data =  request.get_json()
    return login_user(data)


@server.route("/register",methods=["POST"])
def register():
    data = request.get_json()
    return register_user(data)



if __name__ == "__main__":
    server.run(debug=True)
