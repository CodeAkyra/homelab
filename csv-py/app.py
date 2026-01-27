# from flask import Flask, render_template, request
# from netmiko import ConnectHandler

# app = Flask(__name__)


# @app.route("/", methods=["GET", "POST"])
# def index():
#     output = ""
#     if request.method == "POST":
#         device = {
#             # "host": request.form["ip"],
#             # "username": request.form["username"],
#             # "password": request.form["password"],
#             "device_type": "cisco_xe",
#             "host": "208.8.8.50",
#             "username": "admin",
#             "password": "C1sc0123",
#         }

#         conn = ConnectHandler(**device)
#         output = conn.send_command(request.form["command"])
#         conn.disconnect()
#     return render_template("index.html", output=output)


# app.run(debug=True)

# acts like RESTAPI

from flask import Flask, jsonify
from restconf.client import get_interfaces

app = Flask(__name__)


@app.route("/api/interfaces", methods=["GET"])
def interfaces():
    data = get_interfaces()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
