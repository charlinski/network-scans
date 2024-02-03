import requests
from mongodb import addDataToObject, findWhere


def loadCPE(host):
    vendor = host['operating_system'][0]['osclass'][0]['vendor']
    osFamily = host['operating_system'][0]['osclass'][0]['osfamily']
    osName = host['operating_system'][0]['name'].replace('Microsoft ', '').replace(' ','_')
    osGen = host['operating_system'][0]['osclass'][0]['osgen'].replace('X', '*')

    if osFamily == 'Windows' and (osGen =='11' or osGen =='10'): #CPE for Win10 + Win11
        #osFamily = osFamily + '_' + osGen
        resp = requests.get('https://services.nvd.nist.gov/rest/json/cpes/2.0?cpeMatchString=cpe:2.3:o:{}:{}'.format(vendor, osName))

    elif osFamily == 'Windows' and osGen !='11' and osGen !='10': #CPE for any other Windows
        osFamily = osFamily + '_' + osGen
        resp = requests.get('https://services.nvd.nist.gov/rest/json/cpes/2.0?cpeMatchString=cpe:2.3:o:{}:{}'.format(vendor, osFamily))

    else:
        resp = requests.get('https://services.nvd.nist.gov/rest/json/cpes/2.0?cpeMatchString=cpe:2.3:o:{}:{}:{}'.format(vendor, osFamily, osGen))

    try:
        data = resp.json()
        cpes = []
        for cpe in data['products']:
            cpes.append(cpe['cpe']['cpeName'])    
        addDataToObject('address', host['address'], {"operating_system.0.osclass.0.cpe": cpes})
        print('CPEs loaded for', host['address'])

    except:
        print('Could not parse', vendor, osFamily, osGen)

def loadDBObjects():
    hosts = findWhere({"operating_system.osclass.cpe": {"$size": 0} })
    for host in hosts:
        loadCPE(host)

loadDBObjects()

