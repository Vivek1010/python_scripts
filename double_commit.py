#!/user/bin/python
'''
Script to do double commit
Author- Vivek Sheel Banger
Date - 31/MAY/2016
'''
import sys
import time
import subprocess

host = "10.105.226.59" #console server

print("---------Script to to do double commit----------")
folder         = raw_input("please enter the name of the directory where new workspace will be created:  ")
dest_lineup    = raw_input("please enter the name of the lineup where double commit need to be done:  ")
ddts           = raw_input("please enter the DDTS ID :  ")
source_lineup  = raw_input("please enter the source lineup :  ")

print ("------Test Ping------")
p = subprocess.Popen('ping -c4 "%s"'%host, shell=True, stderr=subprocess.PIPE)
#p = subprocess.Popen('acme pull -lineup', 'lineup', shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()

print ("--------getting the Diff from ddts = %s-------" %ddts)

p = subprocess.Popen('acme diff_copy -branch "%s" -changeid "%s" > diff.diff'%(source_lineup,ddts), shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()
print("-------Got the diff -----")

print("------Start pulling the linup =%s" %dest_lineup)
p = subprocess.Popen(['mkdir "%s"'%folder,'cd "%s"'%folder,'acme pull -lineup "%s".lu'%dest_lineup], shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()

print("------GO the workspace -----")

print("------Start patching to dest lineup = %s" %dest_lineup)

p = subprocess.Popen('acme patch -input diff.diff', shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()
print ("------Patching done ------")


print("------Start Double Commit  source  lineup = %s dest lineup  = %s ddts = %s" %(source_lineup,dest_lineup,ddts))

p = subprocess.Popen('/auto/iox/bin/xr_commit -d "%s"'%ddts, shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()
print ("-----XR commit done  ------")

