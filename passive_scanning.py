import pyshark
import socket

from mongodb import findByIp, insertIntoDB
from AppleDevice_identification import check_apple

capture = pyshark.LiveCapture(interface='WLAN')
for packet in capture.sniff_continuously():
    if 'ip' in packet:
        ip = packet['ip'].src
        if findByIp(ip):
            # print('already known', ip)
            pass
        else:
            if '192.168.2' in ip:
                print('New IP:', ip)

                mac = packet.eth.src
                is_apple = check_apple(str(ip))
                if (is_apple == 'apple'):
                    try:
                        hostname = socket.gethostbyaddr(ip)
                        print(hostname)
                    except: 
                        print('Error resolving hostname')
                    insertIntoDB({'host_name': hostname, 'address': ip, 'found': 'passive', 'apple_device': is_apple, 'mac': mac})
                    print('device inserted into db')
                else:
                    try:
                        hostname = socket.gethostbyaddr(ip)
                        print(hostname)
                    except: 
                        print('Error resolving hostname')
                    insertIntoDB({'host_name': hostname, 'address': ip, 'found': 'passive',  'mac': mac})
            else:
                # print('Skip Ip', ip)
                pass