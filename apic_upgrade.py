#/usr/local/bin/python
import pexpect, os, StringIO, sys, datetime, cmd, argparse
host = "10.29.198.36"
user = "admin"
password = "ins3965!"
PROMPT = "#$"
currentdate="01-26-2017"
currenthostname="pod2-apic1"
switch_bootfile="aci-n9000-dk9.12.2.1n.bin"
boot_path="/bootflash/"
switches=["10.0.224.95","10.0.224.94","10.0.224.93"]
def APICLogin():
    child = pexpect.spawn('ssh '+user+'@'+host)
    child.expect ('.*assword:.*')
    child.sendline (password)
    child.expect ('#.*', timeout=10)
    #showTemp(child)
    #scp2Switches(child)
    cleanSwitches(child)
    child.sendline('exit')
    child.close()

def showTemp(child):
    #setting a new file for output")
    fout = file("sh-temp.txt",'w')
    #capturing the command output to the file")
    child.logfile_read = fout
    child.sendline('cd /tmp')
    child.expect(".*# ", timeout=100)
    child.sendline('ls')
    child.expect(".*# ", timeout=100)
    fout.close()

def scp2Switches(child):
    fout = file("scp_out.txt",'w')
    child.logfile_read = fout
    for switch in switches:
        child.sendline('scp %s %s@%s:%s' % (switch_bootfile,user,switch,boot_path))
        i = child.expect(['assword:', r"yes/no"], timeout=30)
        if i == 0:
            child.sendline(password)
        elif i == 1:
            child.sendline("yes")

    fout.close()

def cleanSwitches(child):
    fout = file("clean.txt",'w')
    child.logfile_read = fout
    for switch in switches:
        child.sendline('ssh %s@%s' % (user,switch))
        i = child.expect(['assword:', r"yes/no"], timeout=30)
        if i == 0:
            child.sendline(password)
        elif i == 1:
            child.sendline("yes")
        child.sendline('setup-bootvars.sh %s' % (switch_bootfile))
        child.expect(".*# ", timeout=100)
        child.sendline('setup-clean-config.sh %s' % (switch_bootfile))
        child.expect(".*# ", timeout=300)
        child.sendline('reload')
        child.expect("y/n", timeout=100)

        child.sendline('y')


    fout.close()


def main():


    APICLogin()



main()