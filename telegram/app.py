from flask import Flask, request, jsonify, Response

from core_bot import send_attack_sign, send_doorway_sign

app = Flask(__name__)

@app.route("/atk_sign", methods=["POST"])
def get_data():
    data = request.get_json() # Recebe os dados enviados pelo Google Sheets
    portador = data['portador']
    mods_list = data['mods_list']

    send_attack_sign(portador, mods_list)

    return Response(status=200)


@app.route("/doorway", methods=["POST"])
def get_doorway():
    try:
        data = request.get_json()
        status = data["status"]
        nickname = data["user_nickname"]

        send_doorway_sign(status, nickname)

        return Response(status=200)
    except Exception:
        return Response(status=400)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555)