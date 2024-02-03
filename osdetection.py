import nmap
from mongodb import addDataToObject


def scan_os_detection(network_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=network_range, arguments='-O')
    
    for host in nm.all_hosts():
        ip_address = host
        os_match = nm[host]['osmatch']
        addDataToObject('address', ip_address, {"operating_system": os_match})


network_range = '192.168.2.0/24'   #network range to be scanned

scan_os_detection(network_range)
print('Done.')