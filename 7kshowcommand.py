#/usr/local/bin/python
import pexpect, os, StringIO, sys, datetime, cmd, argparse
host = "10.29.198.33"
user = "admin"
password = "C1sc0123"
PROMPT = "#$"
currentdate="11-19-2014"
currenthostname="N7K"
def N7kLogin():
	child = pexpect.spawn('ssh '+user+'@'+host)
	child.expect ('.*assword:.*')
	child.sendline ("C1sc0123")
	child.expect ('#.*', timeout=10)
	child.sendline ("terminal length 0 ")
	child.expect ('#.*', timeout=10)
	createDir()
	showInterfaces(child)
	showRun(child)
	child.sendline('exit')
	child.close()

def createDir():
    if not os.path.exists(currentdate):
        os.makedirs(currentdate)
    if not os.path.exists(currentdate+"/"+currenthostname):
        os.makedirs(currentdate+"/"+currenthostname)	

def showInterfaces(child):
    #setting a new file for output")
    fout = file(currentdate+"/"+currenthostname+"/"+currenthostname+datetime.datetime.now().strftime("%m-%d-%Y")+"interfaces.txt",'w')
    #fout = file(currenthostname+datetime.datetime.now().strftime("%m-%d-%Y")+"interfaces.txt",'w')
    #capturing the command output to the file")
    child.logfile_read = fout
    #sending show interface")
    
    child.sendline('show interface bri')
    #expect enable mode prompt = timeout 400
    child.expect(".*# ", timeout=100)
    #closing the log file
    #fout.close()

def showRun(child):
    #setting a new file for output")
    fout = file(currentdate+"/"+currenthostname+"/"+currenthostname+datetime.datetime.now().strftime("%m-%d-%Y")+"sh-run.txt",'w')
    #capturing the command output to the file")
    child.logfile_read = fout
    #sending more system running-config")
    child.sendline('show running-config')
    #expect enable mode prompt = timeout 400
    child.expect(".*# ", timeout=999)
    #closing the log file
    fout.close() 

def main():
    #Nothing has been executed yet
    #executing asaLogin function
    N7kLogin()
    #Finished running parTest\n\n Now exiting
    

main()    