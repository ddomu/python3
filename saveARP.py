import json
import re

fiel = "i.json"
ip = "10.1.2.1"
#filename is ip address
# f = open(fiel, 'r')

l = json.loads(ip)

va={}
ipmaif = [] # ip,mac,if
# IP Search in ARP table # 
for k, v in l.iteritems():
 print (k)
 for line in v[0:5]:
  print (line)
  if "Interface" in line : # header line  
    headers = re.split("\s\s+", line)
    ip_index = headers.index("Address") 
    mac_hw = "Hardware Addr" if "Hardware" in line else "MAC Address"  # MAC Address or Hardware Addr 
    mac_index = headers.index(mac_hw) 
    if_index = headers.index("Interface") 
  elif bool(ip_pattern.search(line)) : # IP address exists
# elif bool(mac_pattern.search(line)) : # MAC address exists  
    contents = re.split("\s\s+", line)
    if ip_index and mac_index and if_index : 
     ipmaif.append([ip,k ] + map(contents.__getitem__, [ ip_index, mac_index, if_index] ))
     #print (contents[if_index])
  else:
    #print ("no mac", line)
    print ("--------------")
# va[k] = ipmaif      
for i in ipmaif[0:30]:
  print (i)
 
 
# mac_pattern = re.compile(r'([0-9A-F]{4})' + '\.([0-9A-F]{4})'*2, re.IGNORECASE)
# mac_pattern = re.compile(r'([0-9A-F]{4})' + '\.([0-9A-F]{4})'*2, re.IGNORECASE)
mac_pattern = re.compile(r'([0-9A-F]{4})' + '[\.:-]([0-9A-F]{4})'*2, re.IGNORECASE) # Update deliminator 

ip_reg_exp = '[1-9](\d{0,2})(\.\d{1,3}){3}'
ip_pattern = re.compile(ip_reg_exp)

# NX OS Header 
#"Address         Age       MAC Address     Interface"

# IOS Header
#"Protocol  Address          Age (min)  Hardware Addr   Type   Interface"


#### Get file list in directory 
from os import listdir
from os.path import isfile, join


mypath = "./arp"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
ip=onlyfiles[-1]
