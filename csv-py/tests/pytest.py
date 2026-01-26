
# connect to device using netmiko and allows the user to enter password and secret at runtime for better security.

from netmiko import ConnectHandler
from getpass import getpass

# cisco1 = ConnectHandler(
#     device_type='cisco_xe',
#     host='208.8.8.50',
#     username='admin',
#     password= 'C1sc0123',
#     secret= "C1sc0123",
#     # password=getpass('Enter device password: '),
#     # secret=getpass('Enter enable secret: '),
#     port='22',
# )

# print(net_connect.find_prompt())
# net_connect.disconnect()

# 
cisco2 = {
    "device_type":'cisco_xe',
    "host":'208.8.8.50',
    "username":'admin',
    "password": 'C1sc0123',
    "secret": "C1sc0123",
    # password=getpass('Enter device password: '),
    # secret=getpass('Enter enable secret: '),
    "port":'22',
}

net_connect = ConnectHandler(**cisco2)

config = [
    "ip sla 1",
    "icmp-echo 208.8.8.2",
    "frequency 5",
    "ip sla schedule 1 life forever start-time now"
]

net_connect.send_config_set(config)

output = net_connect.send_command("show ip sla statistics 1")
print(output)


# print(net_connect.find_prompt())
net_connect.disconnect()
