#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" utils.py -- utilities for ARP man in the middle """

import subprocess as sp
import os as os
import binascii
from numpy import delete
import random
import sys
from threading import Thread
import time
import re


def format_output(sortie):
    sortie = sortie.replace("\n","")
    sortie = sortie.replace(" ","")
    return sortie

def inttobin8(num):
    i = 7;
    returnValue = ""
    num = int(num)
    while i >= 0:
        returnValue += str(int(num/(2**i)))
        num = num%(2**i)
        i -= 1
    return returnValue
    
def bin8toint(num):
    i = 0
    returnValue = 0
    while (i < 8):
        returnValue += 2**i * int(num[7-i])
        i += 1
        
    return returnValue

def inttoIP(IP):
    
    outputIP = ""
    i = 0
    
    while(i < 4):
        i+=1
        outputIP = str(IP % 256) + "." + outputIP
        IP = IP // 256
                    
    return outputIP[:-1]
    
def multitool(args):
    return format_output(os.popen("./multitool.sh " + args).read())

def CIDR_find(initialNetmask):
    binNetmask = bin(initialNetmask)
    CIDR = 0
    while binNetmask[CIDR+2] == "1":
        CIDR += 1
    return CIDR
    
def formatIP(sourceIP):
    tablIP = sourceIP.split(".")
    binIP = ""
    for num in tablIP:
        binIP += inttobin8(num)
    return int(binIP, 2)
    
def isIP(test):
    return re.match(r"^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$",test) != None

def areIP(test):
    value = True
    for i in test:
        if isIP(i) != True:
            value = False
    return True

