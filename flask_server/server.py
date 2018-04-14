from flask import Flask
from controller.dao import get_user_info
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login/<username>/password/<password>", methods=['GET'])
def valid(username, password):
    result = get_user_info(username, password)
    if result:
        return result[2]
    return 'Fail', 500

if __name__ == '__main__':
    app.run( port=8000, debug=True)