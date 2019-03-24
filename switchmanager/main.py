from getpass import getpass
from netmiko import Netmiko
from Switch import Switch
import mainMenu
import interpreter

host = input("Host: ")
username = input("Login: ")
password = getpass()

edge1 = {
    "host": host,
    "username": username,
    "password": password,
    "secret": password,
    "device_type": "ubiquiti_edge",
}

net_connect = Netmiko(**edge1)

switch = Switch(interpreter.getDeviceName(net_connect.find_prompt()))
print(switch.getName())

while True:
    print(mainMenu.printMenu())
    choice = input("Choose: ")
    if choice == "1":
        command = "show vlan"
    elif choice == "2":
        command = "show vlan port all"
    elif choice == "9":
        net_connect.disconnect()
        break
    else:
        print("error")
    print()
    output = net_connect.send_command(command)
    print(output)
    print()