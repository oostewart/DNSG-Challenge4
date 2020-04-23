

import ipaddress
import json

# Open file object in working script directory and load as it as JSON data.
# The 'with' statement provides a way to automatically close the file and clean-up.
with open('JSONdata') as file:
    data = json.load(file)

# Definite JSON value and iterates through the data file 'for'
# Use 'try' error exception handling to validate the value "lanIP" using the import ipaddress module
for value in data:
    ipv4 = value['lanIp']
    sn = value['serial']    
    try:
        ipaddress.IPv4Address(ip)
        print(ipv4 + ' is a valid IP address for Serial ' + sn)
    except ValueError:
        print(ipv4 + ' is NOT a valid IP address for Serial ' + sn)
