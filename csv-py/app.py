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
# cisco UI command tool / informative app using python and some framework and libraries etc etc :D

from flask import Flask, jsonify, request, render_template
from netmiko import ConnectHandler

app = Flask(__name__)

COMMANDS = {
    "interfaces": "show ip interface brief",
    "routes": "show ip route",
    "version": "show version",
    "clock": "show clock",
    "cdp": "show cdp",
    "lldp": "show lldp",
    "lldp run": "lldp run",
    "cdp run": "cdp run",
}

DEVICE = {
    "device_type": "cisco_xe",
    "host": "208.8.8.50",
    "username": "admin",
    "password": "C1sc0123",
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run", methods=["POST"])
def run_command():
    action = request.json.get("action")

    if action not in COMMANDS:
        return jsonify({"error": "Invalid command"}), 400

    conn = ConnectHandler(**DEVICE)
    output = conn.send_command(COMMANDS[action])
    conn.disconnect()

    return jsonify({"output": output})


if __name__ == "__main__":
    app.run(debug=True)
