from getpass import getpass
from netmiko import ConnectHandler
import paramiko
import json
import logging


# Enable debugging
logging.basicConfig(
    filename="netmiko_debug.log",
    level=logging.DEBUG,
)

# Allow legacy SSH algorithms for compatibility with the device.
paramiko.Transport._preferred_kex = (
    "diffie-hellman-group1-sha1",
    *paramiko.Transport._preferred_kex,
)

paramiko.Transport._preferred_keys = (
    "ssh-rsa",
    *paramiko.Transport._preferred_keys,
)

paramiko.Transport._preferred_ciphers = (
    "aes128-cbc",
    *paramiko.Transport._preferred_ciphers,
)

# Device connection information
device_dict = {
    "device_type": "cisco_wlc",
    "host": "192.168.1.193",
    "username": "drift",
    "password": getpass("Enter device password: "),
    "conn_timeout": 15,
    "banner_timeout": 15,
    "auth_timeout": 15,
    "session_log": "session.log",
}

try:
    with ConnectHandler(**device_dict) as c:
        print("SSH connection successful!")

        # Collect device information
        report = {
            "hostname": c.send_command("show running-config | include hostname"),
            "program_version": c.send_command("show version | include Version"),
            "device_model": c.send_command("show version | include Cisco CISCO"),
            "interfaces": c.send_command("show ip interface brief"),
        }












    

    # Display report
    for key, value in report.items():
        print(f"{key.replace('_', ' ').title()}:")
        print(value)
        print()

    # Save JSON report
    with open("rapport.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print("Report saved to rapport.json")

except Exception as error:
    print(f"Connection or execution failed: {type(error).__name__}: {error}")
    print("Check netmiko_debug.log and session.log for details.")