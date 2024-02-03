import requests
from mongodb import addDataToObject, findAll


def loadCVE(name, severity):
    print('start req')
    if 'cpe:2.3:o:' in name:
        name = name.replace('cpe:2.3:o:', '')
    resp = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0?cvssV3Severity={}&cpeName=cpe:2.3:o:{}'.format(severity, name))
    print('end req')
    try:
        data = resp.json()
        return len(data['vulnerabilities'])
    except:
        print('Could not parse', severity, name)


def attachCVEs():
    hosts = findAll()
    
    for host in hosts:
        host_Name = host['host_name']
        try:
            if 'operating_system' in host:
                os = host['operating_system'][0]
                osclasses = os['osclass']
                for osclass in osclasses:
                    cpes = osclass['cpe']
                    if len(cpes) > 0:
                        for cpe in cpes:
                            cpe_name = cpe.replace('cpe:/o:', '')
                            number_of_cves_low = loadCVE(cpe_name, 'LOW')
                            number_of_cves_medium = loadCVE(cpe_name, 'MEDIUM')
                            number_of_cves_high = loadCVE(cpe_name, 'HIGH')
                            number_of_cves_critical = loadCVE(cpe_name, 'CRITICAL')
                            print(host_Name, cpe_name, number_of_cves_low, number_of_cves_medium, number_of_cves_high, number_of_cves_critical)
                            addDataToObject('address', host['address'], {"cve_cvss": {"low": number_of_cves_low, "medium": number_of_cves_medium, "high": number_of_cves_high, "critical": number_of_cves_critical}})
        except:
            print('Error with host: ', host_Name)
attachCVEs()