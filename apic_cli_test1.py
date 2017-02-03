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

if channel_data.endswith('rtp2-apic1#'):
	print '### ENDS with rtp2-apic1# sending...'
	channel.send('show tenant common\n')
        print '### SENDING return'
	channel.send('\n')
	print "N is n"

	channel_data = channel.recv(9999)
	print 'CHANNEL DATA: ' + channel_data
