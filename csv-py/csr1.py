# config router muna

# enable
#     config t
#         username admin privilege 15 secret C1sc0123
#         ip domain-name CSR1000V
#         hostname CSR-TEST-PY
#         crypto key generate rsa
#             2048
#         line con 0
#             login local
#             exec-timeout 0 0
#             exit
#         line vty 0 4
#             login local
#             exec-timeout 0 0
#             transport input ssh
#             exit
#         int g1
#             ip add 208.8.8.50 255.255.255.0
#             no shut
#             exit
#         crypto pki trustpoint RESTCON-TP
#             enrollment selfsigned
#             subject-name CN=CSR-TEST-PY
#             rsakeypair RESTCON-KEY
#             exit
#         crypto pki enroll RESTCON-TP
#             no
#             yes
#             208.8.8.50
#             yes
#         ip http secure-server
#         ip http secure-trustpoint RESTCON-TP
#         restconf
#         end

#         do sho ip http server secure status

# My very first py script connection to Cisco_XE router using netmiko

from netmiko import ConnectHandler

csr1 = {
    'device_type': 'cisco_xe',
    'host': '208.8.8.50',
    'username': 'admin',
    'password': 'C1sc0123',
    'secret': 'C1sc0123',
    'port': '22',
}

conn = ConnectHandler(**csr1)
conn.enable()

output = conn.send_command('show ip interface brief')
print(output)


#this script connects to the cisco xe router and runs the show ip int br command and prints the output to the console