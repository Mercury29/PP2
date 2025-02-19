import json
with open(r'C:\Users\Merc\Downloads\KBTU\PP2\lab4\lab.json', 'r') as file:
    data = json.load(file)
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)
for item in data["imdata"]:
    if "l1PhysIf" in item:
        interface = item["l1PhysIf"]["attributes"]
        dn = interface.get('dn', 'N/A')
        description = interface.get('descr', 'N/A') or "N/A"  
        speed = interface.get('speed', 'N/A')
        mtu = interface.get('mtu', 'N/A')
        print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")