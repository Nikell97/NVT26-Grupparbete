from getpass import getpass
from netmiko import ConnectHandler
import json

#dict containing the device information neccessary for ConnectHandler to establish ssh connection
device_dict = {
    "device_type": "cisco_ios",
    "host": "192.168.1.193",
    "username": "drift",
    "password": getpass("Enter device password: "),
}

# establishes connection with device through ConnectHandler creates a new dict called report and saves the fetched values to it
with ConnectHandler(**device_dict) as c:
    report = {
        "hostname": c.send_command("show running-config | include hostname"), # fetches only line with hostname from running config
        "program_version": c.send_command("show version | include Version"), # fetches only line with program version
        "device_model": c.send_command("show version | include Cisco CISCO"), # fetches only the line with device model
        "interfaces": c.send_command("show ip interface brief"), # fetches information about device interfaces
    }

# Loop to display all information from the report dict
for key, value in report.items():
    print(f"{key.replace('_', ' ').title()}:")
    print(value)
    print()

# Save report dict as JSON file
with open("rapport.json", "w", enconding="utf-8") as file:
    json.dump(report, file, indent=4, ensure_ascii=False)

print("Report saved to rapport.json")

