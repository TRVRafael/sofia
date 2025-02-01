from flask import Flask, request, jsonify, Response
from main import exec_hide_area

app = Flask(__name__)

@app.route("/hide", methods=["GET"])
def get_data():
    exec_hide_area()



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=54444)