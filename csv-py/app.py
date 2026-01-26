from flask import Flask, render_template, request
from netmiko import ConnectHandler

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        device = {
            "device_type": "cisco_xe",
            "host": request.form["ip"],
            "username": request.form["username"],
            "password": request.form["password"],
        }

        conn = ConnectHandler(**device)
        output = conn.send_command(request.form["command"])
        conn.disconnect()

    return render_template("index.html", output=output)

app.run(debug=True)
