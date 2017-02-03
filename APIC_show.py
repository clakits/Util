import time
from collections import defaultdict
import sys
import re
import socket
import paramiko

def tree():
    return defaultdict(tree)
t = tree()

def ssh_auth(device, name):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device, username='admin', password='ins3965!',timeout=5)
        return ssh
    except paramiko.AuthenticationException:
        print "Please check username for %s %s"%(device, name)
        return None
    except socket.error:
        print "connection failed for %s %s "%(device, name)
        return None

def commandexecution(ip, name):
    ssh = ssh_auth(ip, name)
    if ssh :
    	show_lst = [('hostname','show controller')]
    	for command_type, command in show_lst:
    	    stdin, stdout, stderr = ssh.exec_command(command)
    	    for resp in stdout.readlines():
    	    	t[name][command_type] = resp.strip()

    	ssh.close()


device_lookup_d = { 
'10.122.254.141':'rtp2-apic1',

 }


for ip, name in device_lookup_d.iteritems():
    commandexecution(ip, name)
    
for name, data in t.iteritems():
    for command, output in data.iteritems():
        print '%s has hostname %s'%(name, output)
