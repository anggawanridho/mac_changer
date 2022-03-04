#/usr/bin/env python3

import subprocess

subprocess.call("ifconfig", shell=True)
interface = input("interface : ")
new_mac = input("new mac address for %s : " %interface)
print("[+] changing config for %s to mac %s " %(interface,new_mac))

subprocess.call(["ifconfig", interface])
#subprocess.call(["ifconfig", interface, "down"])
#subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#subprocess.call(["ifconfig", interface, "up"])
