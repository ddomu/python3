# Get ARP/ MAC 
##---------------- PHASE 2 -----------------#

### To Do List (by Order of Importance) 
1. Add Palo Alto and F5 arp
2. Get switches interface Access port / Trunk Port 
3. CSV Export 
4. VRF Dropdown 
mac address input form - any format 

### Palo Arp 
' key 
LUFRPT1acEhZN2pkalRobWE3V2szb29kaWdPMVQrWU09SFZRbzVIamtRR0VyQmJLRWQ0RFljeHIxZyswSnZieWE1ajVTT2RJT1NRbz0=

https://10.181.101.60/  https://10.181.101.61/
https://10.200.84.14/   https://10.200.84.15


https://10.181.101.61/api/?&type=op&cmd=%3Cshow%3E%3Carp%3E%3Centry+name+%3D+%27all%27%2F%3E%3C%2Farp%3E%3C%2Fshow%3E&key=LUFRPT1acEhZN2pkalRobWE3V2szb29kaWdPMVQrWU09SFZRbzVIamtRR0VyQmJLRWQ0RFljeHIxZyswSnZieWE1ajVTT2RJT1NRbz0=


##---------------- PHASE 1 -----------------# 
Ansible/ python cron job 

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

#### Views.py
list view 

```
## DRF ( Rest API framework ) 
* ArpTable
* MacTable

GetARP/MACtable search result first 10 
news = News.objects.order_by("-date")[:10] 


# Save ARP to DB
 file directory : ~/data/arp/* 
 
 get_arp for all file 
 ```
 get_arp.py 
 
 ```
 return list [ ]  
 
 

# Save MAC to DB 

 file directory : ~/data/mac/* 
 
 get_mac for all file 
 ```
 get_mac.py 
 
 ```
 return list [ ]  


(tutorial-env) [hpark84@mrpdcnnetapp parse]$ python
Python 3.6.5 (default, Jul 25 2018, 21:22:33) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from get_mac import *
>>> mac_list = get_macs()
>>> len(mac_list)
860475
??? max limit to push mysql query 
real	3m51.752s
user	0m31.614s
sys	0m7.525s


# TO- DO 
 distribute of ansible running for several groups  +2,200 devices 
 
 ## Pagenation : 초보몽키 기술 


