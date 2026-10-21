import json
with open("../rapport.json", "r", encoding="utf-8") as fil:
    rapport = json.load(fil)

    print("Router:", rapport["hostname"])
    print("Modell:", rapport["device_model"])
    print("IOS-version:", rapport["program_version"])
    antal_up = 0
    antal_down = 0
    for interface in rapport["interfaces"].splitlines():
        print(interface)
        if interface.split()[-2:] == ["up", "up"]:
            antal_up += 1
        elif interface.split()[-2:] == ["down", "down"] and "administratively" not in interface:
            antal_down += 1
print("Antal aktiva gränssnitt:", antal_up)
print("Antal nere gränssnitt:", antal_down)