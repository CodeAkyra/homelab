# script to generate all necessary router health check data and save to a file

from netmiko import ConnectHandler
from datetime import datetime


COMMANDS = {
    "interfaces": "show ip interface brief",
    "interface_errors": "show interfaces",
    "cpu": "show processes cpu | exclude 0.00%",
    "routes": "show ip route",
    "logs": "show logging | include LINEPROTO|SYS|ERROR|WARN",
}

DEVICE = {
    "device_type": "cisco_xe",
    "host": "208.8.8.50",
    "username": "admin",
    "password": "C1sc0123",
    "secret": "C1sc0123",
}


def main():
    print("\n📡 Connecting to router...")
    conn = ConnectHandler(**DEVICE)
    conn.enable()

    report = []
    report.append(f"🕒 Health Check Report - {datetime.now()}\n")

    for title, cmd in COMMANDS.items():
        output = conn.send_command(cmd)
        report.append(f"\n==== {title.upper()} ====\n{output}")

    conn.disconnect()

    filename = f"router_health_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print(f"✅ Health check complete. Report saved as {filename}")


if __name__ == "__main__":
    main()
