import nmap
from AppleDevice_identification import check_apple
from mongodb import findByIp, insertIntoDB


def host_discovery_scan(network_range):
    nm = nmap.PortScanner()

    nm.scan(hosts=network_range, arguments='-sn') #host discovery on specified network range
    
    # Iterate over the list of scanned hosts
    for host in nm.all_hosts():
        ip_address = host
        host_name = nm[host].get('hostnames', [{}])[0].get('name', 'N/A')
        status = nm[host]['status']['state']

        if 'mac' in nm[host]['addresses']:
            mac = nm[host]['addresses']['mac']
            print(mac)
        print(nm[host]['addresses'])

        print(f"IP Address: {ip_address}\tHost Name: {host_name}\tStatus: {status}")
        dbObject = findByIp(ip_address)
        if not dbObject:
            is_apple = check_apple(ip_address)
            hostInstance = { "host_name": host_name, "address": ip_address, 'status': status, 'mac': mac, 'apple_device': is_apple}
            insertIntoDB(hostInstance)
        
        
network_range = '192.168.2.0/24' #network range to be scanned

host_discovery_scan(network_range)