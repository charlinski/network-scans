# leveraging network data for automated host discovery and vulnerability management
## 1. Setup
Code must be run with admin privileges
docker-compose up -d
activate venv: for more information refer to:  https://docs.python.org/3/library/venv.html

Tools used: 
* nmap
* pyshark
## 2. Execution


### Order of Execution:
1. mongodb.py 

2. hostdiscovery.py
**required input:** network range in l.30

3. passive_scanning.py
**required input:** 
a) (if needed) change interface to sniff in l.7 
b) replace network range input in l.16 ('192.168.2') as required for the network to be scanned

4. osdetection.py
**required input:** network range in l.15

5. loadCPE.py

6. loadCVE.py 



## 3. Important Notes
**Apple_Device_identification.py:** 
It is not required to run Apple_Device_identification.py individually, as the file contains only a function. 

**Nmap in WSL:**
Code cannot be run in a WSL, as Nmap will only scan on the WSL network. Bridge from WSL to actual network is required.

**Load of APIs:**
Depemnding on the load of the APIs, it can sometimes take a little longer to receive a response from the APIs.

**Admin privileges:**
Admin priviliges are required to run the code.
