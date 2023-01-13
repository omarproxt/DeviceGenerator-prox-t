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
