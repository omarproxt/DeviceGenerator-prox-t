import os
os.system ('clear')
import requests, pyfiglet,time,sys,webbrowser 
Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
logo = pyfiglet.figlet_format('omarproxt')
print(a_bSa+logo)
from hmac import new
from os import urandom
from hashlib import sha1
from progress.bar import IncrementalBar

def generate_device_id(identifier: str):
	return ("52" + identifier.hex() + new(bytes.fromhex("02b258c63559d8804321c5d5065af320358d366f"), b"x42" + identifier, sha1).hexdigest()).upper()

def generation_process(count: int):
    progress_bar = IncrementalBar("Generated", max=count)
    with open("omarproxt", "a") as file:
    	for i in range(count):
    		device_id = generate_device_id(urandom(20))
    		file.write(f"{device_id}\n")
    		progress_bar.next()
    	progress_bar.finish()
    	print(f"Generated {count} deviceIDs")
    
generation_process(count=int(input("How much deviceID generate••>>")))

print('\033[1;33mThe device is stored at omarproxt\033[1;91m')
