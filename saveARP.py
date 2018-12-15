#### Get file list in directory 
from os import listdir
from os.path import isfile, join

directory = "./arp" # directory 
onlyfiles = [f for f in listdir(directory) if isfile(join(mypath, f))]

## RETURN onlyfiles 


##### Get [ip_address, mac_address, interface] list

import json
import re

# mac_pattern = re.compile(r'([0-9A-F]{4})' + '\.([0-9A-F]{4})'*2, re.IGNORECASE)
# mac_pattern = re.compile(r'([0-9A-F]{4})' + '\.([0-9A-F]{4})'*2, re.IGNORECASE)
mac_pattern = re.compile(r'([0-9A-F]{4})' + '[\.:-]([0-9A-F]{4})'*2, re.IGNORECASE) # Update deliminator 

ip_reg_exp = '[1-9](\d{0,2})(\.\d{1,3}){3}'
ip_pattern = re.compile(ip_reg_exp)


#!! Test for last ip file 
ip=onlyfiles[-1]
with open(directory+"/"+ip) as fp:
    data = json.load(fp)
  
va={}
ipmaif = [] # ip,mac,if
# IP Search in ARP table # 
#for k, v in l.iteritems():
for vrf, contents in data.items():
 print (vrf)
# for line in v[5:20]:
 for line in contents:
  if "Interface" in line : # header line 
    print (line)
    headers = re.split("\s\s+", line)
    ip_index = headers.index("Address") 
    mac_hw = "Hardware Addr" if "Hardware" in line else "MAC Address"  # MAC Address or Hardware Addr 
    mac_index = headers.index(mac_hw) 
    if_index = headers.index("Interface") 
  elif bool(ip_pattern.search(line)) : # IP address exists
# elif bool(mac_pattern.search(line)) : # MAC address exists  
    contents = re.split("\s\s+", line)
    if headers: 
     ipmaif.append([ip,vrf ] + list(map(contents.__getitem__, [ ip_index, mac_index, if_index]) ))
     #print (contents[if_index])
  else:
    #print ("no mac", line)
    print ("--------------")
# va[k] = ipmaif      


for i in ipmaif[0:30]:
  print (i)

 

# NX OS Header 
#"Address         Age       MAC Address     Interface"

# IOS Header
#"Protocol  Address          Age (min)  Hardware Addr   Type   Interface"


