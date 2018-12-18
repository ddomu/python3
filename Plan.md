# Get ARP/ MAC 
## method : Ansible 
#### ARP 
 1. BGP neighbor from Edge 
 2. Sort out neighbors os type and prepare inventory for ios, nxos 
 3. running show ip arp vrf {{ vrf.name }} 
 4. save  dictionary to json format file  { "vrf name": [stdout_lines] } 
#### MAC 
 1. start with statseeker ping device list +2,000 devices 
 2. get rid of any BGP neighbor list and prepare inventory file 
 3. running show mac address for all devices 
 4. save "show mac addr" result as dictionary { 'hostname': swt, 'error': "" , 'result' : "mac table string "  } 


# Django App creation 
## App name : mist (mac ip search tool) 
```
device_ip, vrf_name, arp_ip, arp_mac, arp_if 

```

# Save ARP to DB
 file directory : ~/data/arp/* 
 
 get_arp for all file 
 ```
 get_arp.py 
 
 ```
 return list [ ]  
 
 
# Save MAC to DB 
