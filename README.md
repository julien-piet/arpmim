# arpmim -- Simple arp man in the middle using arp-sk

WARNING - This is not a stable tool, it will make your network crash. Use with caution. 


**********
SYNTAX
**********

arpmim.py [-c ALICE_IP BOB_IP | IP_1 IP_2 [...]]

**********
DESCRIPTION
**********

arpmim will perform an ARP man-in-the-middle attack using arp-sk.
* If no argument is given, it will perform it between each device on the network and the router
* If the -c flag is given with two IPs, it will perform a MITM between both these IPs
* If no flag is given but a list of IPs instead, it will do a MITM between each IP and the router

**********
KNOWN ISSUES
**********

Killing the process can be difficult because of multithreading. Need to implement more robust SIGINT handling
