import json
import re

fiel = "i.json"

# f = open(fiel, 'r')

l = json.loads(i)

# IP Search in ARP table # 
for k, v in l.iteritems():
 print (k)
 for line in v[0:5]:
  # print (line)
  if "Interface" in line : # header line 
    headers = re.split("\s\s+", line)
    print (headers) 
  elif bool(ip_pattern.search(line)) : # MAC address exists  
    print (line)
  else:
    #print ("no mac", line)
    print ("--------------")
      
  
#  mac_pattern = re.compile(r'([0-9A-F]{4})' + '\.([0-9A-F]{4})'*2, re.IGNORECASE)
mac_pattern = re.compile(r'([0-9A-F]{4})' + '\.([0-9A-F]{4})'*2, re.IGNORECASE)

mac_pattern = re.compile(r'([0-9A-F]{4})' + '[\.:-]([0-9A-F]{4})'*2, re.IGNORECASE)

ip_reg_exp = '[1-9](\d{0,2})(\.\d{1,3}){3}'
ip_pattern = re.compile(ip_reg_exp)

# MAC  Search in ARP table # 
for k, v in l.iteritems():
 print (k)
 for line in v[0:5]:
  # print (line)
  if "Interface" in line : # header line 
    headers = re.split("\s\s+", line)
    print (headers) 
  elif bool(mac_pattern.search(line)) : # MAC address exists  
    print (line)
  else:
    print ("no mac", line)
    #print ("--------------")
    
