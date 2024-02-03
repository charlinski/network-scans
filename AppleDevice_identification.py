import nmap


def check_apple(host: str):
    port_open_62078 = False
    port_open_5353 = False
    
    nm = nmap.PortScanner()
    nm.scan(hosts=host, arguments='-p 62078') #scans the iphone-sync TCP port

    if host in nm.all_hosts():
        try:
            if 'open' in nm[host]['tcp'][62078]['state'] and 'iphone-sync' in nm[host]['tcp'][62078]['name'] :
                #print(nm[host])
                port_open_62078 = True
        except:
            return 'is-apple'
      
    nm.scan(hosts=host, arguments='-sU -p 5353') #scans the UDP port  
    if host in nm.all_hosts():
        try:
            if 'open' in nm[host]['udp'][5353]['state']:
                port_open_5353 = True
                if port_open_5353 and port_open_62078:
                    #print(nm[host])
                    return 'is-apple'
        except:
            return 'not-apple'
    
    return 'not-apple'
