import os
import random
import netifaces
import re
import uuid
import time
os.system("sudo service NetworkManager restart")
print(" ")
print(" ")
print (" \033[1;31;40m The MAC address is : ", end="")
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))
print(" ")
print(" \033[1;32;40m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(" \033[1;34;40mChoose Your Network Interface Card")
print(" ")
print(" \033[1;32;40m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
if_list = str(netifaces.interfaces())
s1=re.sub("[''$@&]","",if_list)
print(" ")
print("__________ \033[1;31;40m" + s1 +" \033[1;32;40m__________")
print(" ")
network_check = input(">>>>>>  \033[1;33;40m")
time.sleep(2)
os.system("sudo service NetworkManager restart")
time.sleep(2)
os.system(f"sudo ifconfig {network_check} down")
os.system(f"sudo ifconfig {network_check} hw ether {random.choice(list(open('mac.txt')))}")
os.system(f"sudo ifconfig {network_check} up")
time.sleep(1)
print(" ")
os.system(f"sudo ifconfig {network_check} ")