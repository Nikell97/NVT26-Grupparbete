from getpass import getpass
from netmiko import ConnectHandler
import paramiko
import json
import logging
import os

#Intro Jennie

#Mattias
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

    # Martin
    if os.path.exists("rapport.json"):
        with open("rapport.json", "r", encoding="utf-8") as fil:
            rapport = json.load(fil)

            print("\n" + "=" * 100)
            print(" HISTORISK RAPPORT (FRÅN FIL)".center(100))
            print("=" * 100)
            print("Router:     ", rapport["hostname"])
            print("Modell:     ", rapport["device_model"])
            print("IOS-version:", rapport["program_version"])
            print("-" * 100) # Avdelare innan gränssnitten börjar
            
            antal_up = 0
            antal_down = 0
            for interface in rapport["interfaces"].splitlines():
                print(interface)
                if interface.split()[-2:] == ["up", "up"]:
                    antal_up += 1
                elif interface.split()[-2:] == ["down", "down"] and "administratively" not in interface:
                    antal_down += 1
                    
        print("-" * 100) # Avdelare efter gränssnitten
        print("Antal aktiva gränssnitt:", antal_up)
        print("Antal nere gränssnitt:  ", antal_down)

    #Riso
    print("\n" + "=" * 100)
    print(" NY LIVE-RAPPORT (FRÅN ROUTER)".center(100))
    print("=" * 100)
    print("Router:     ", report["hostname"])
    print("Modell:     ", report["device_model"])
    print("IOS-version:", report["program_version"])
    print("-" * 100)
    
    antal_up_ny = 0
    antal_down_ny = 0
    
    for interface in report["interfaces"].splitlines():
        print(interface)
        if interface.split()[-2:] == ["up", "up"]:
            antal_up_ny += 1
        elif interface.split()[-2:] == ["down", "down"] and "administratively" not in interface:
            antal_down_ny += 1
            
    print("-" * 100)
    print("Antal aktiva gränssnitt:", antal_up_ny)
    print("Antal nere gränssnitt:  ", antal_down_ny)
    print("=" * 100 + "\n")
    
    # Display report
    """for key, value in report.items():
        print(f"{key.replace('_', ' ').title()}:")
        print(value)
        print()"""

    #Hanna
    # Save JSON report
    with open("rapport.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print("Report saved to rapport.json")

except Exception as error:
    print(f"Connection or execution failed: {type(error).__name__}: {error}")
    print("Check netmiko_debug.log and session.log for details.")