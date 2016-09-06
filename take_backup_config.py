#!/usr/bin/python
 
import telnetlib
import datetime
 
now = datetime.datetime.now()
 
host = "5.24.7.5" # your router ip
username = "root" # the username
password = "root"
filename_prefix = "cisco-backup"
 
tn = telnetlib.Telnet(host)
tn.read_until("Username:")
tn.write(username+"\n")
tn.read_until("Password:")
tn.write(password+"\n")
tn.write("terminal length 0"+"\n")
tn.write("sh run"+"\n")
tn.write("exit"+"\n")
output=tn.read_all()
 
filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)
 
fp=open(filename,"w")
print output
fp.write(output)
fp.close()
