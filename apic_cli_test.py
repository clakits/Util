# -*- coding: utf-8 -*-
# coding=<utf-8>
import paramiko
import os
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.122.254.141', port=22, username='admin', password='ins3965!')
channel = ssh.invoke_shell()
channel_data = str()
host = str()
srcfile = str()
n = 1
while n < 5:
	if channel.recv_ready():
		channel_data += channel.recv(9999)
		print '#### Device Output ####'
		print channel_data
		print '\n#############'
	else: 
		continue

	if channel_data.endswith('rtp2-apic1#'):
		print '### ENDS with rtp2-apic1# sending...'
		channel.send('show tenant common\n')
                print '### SENDING return'
		channel.send('\n')

		n = n + 1
		print "N is n"

	elif channel_data.endswith('>'):
		channel.send('execsh\n')
		n = n + 1

	elif '(Timed out)' in channel_data:
		print '\nERROR:'
		channel_data = ''
		channel.send('\n')
