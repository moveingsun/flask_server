from flask import Flask, jsonify, request
from controller.dao import get_user_info, get_article_info, register_user
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/login/<username>/password/<password>", methods=['GET'])
def valid(username, password):
    result = get_user_info(username, password)
    if result:
        returndict = {'role':result[2]}
        res = jsonify(returndict)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    return 'Fail', 500


@app.route("/article/<title>/", methods=['GET'])
def getarticle(title):
    result = get_article_info(title)
    if result:
        returndict = {'content':result[2]}
        res = jsonify(returndict)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    return 'Fail', 500


@app.route("/user/adduser/<username>/password/<password>", methods=['GET'])
def registeruser(username, password):
    user = {'username': username, 'password': password}
    if register_user(user):
        return 'Success'
    return 'Fail', 500


@app.after_request
def apply_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response


if __name__ == '__main__':
    app.run(port=8000, debug=True)