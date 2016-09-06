'''
Script to reset line of console server
Author- Vivek Sheel Banger
Date - 2/Feb/2016
'''
import telnetlib
import sys
import time

host = "10.105.226.59" #console server
username = ""       #username
password = ""       #pasword

ch = raw_input("please enter 1 if serve if 10.105.226.44 else just enter for 10.105.226.59 : ")
if ch == '1':
    host = "10.105.226.44"

if len(sys.argv) == 1:
    line = raw_input("enter the line no to close  : ")   #input for line no
else:
    line = sys.argv[1]  #input for line no

tn = telnetlib.Telnet(host)
print "Connecting console server " + host
tn.read_until("Username:")
tn.write(username+"\n")
tn.write(password+"\n")
tn.read_until("#")
print "closing the connection for line " + line
tn.write("clear line "+line+ "\n")
tn.read_until("[confirm]")
tn.write("\n")
tn.read_until("#")
print "exiting now"

'''
tn.write("help \n")
data = '' 
while data.find('#') == -1:
    time.sleep(1)
    data = tn.read_lazy()
    print data
#print tn.read_all()
'''
tn.write("exit \n")
tn.close
