#!/usr/bin/env python

# __author__     = "Vivek Banger"
# __copyright__  = "Copyright 2016,"
# __credits__    = ["", "", "", ""]
# __license__    = "GPL"
# __version__    = "0.1"
# __maintainer__ = ""
# __email__      = "vbanger@cisco.com"
# __status__     = "non-Production"

from __future__ import print_function
import re

#global varriables
if_list    = []
state_list = []
dest_list  = []
diag_list  = []

# This function will print NP Counters
# if any
def serch_for_np_counter():
      print ("NP_CPOUNTER_PRINT")
      return 


# get the user input,never trust user
while(True):
    try:
      print ("Enter a file name:",end = "")
      filename = raw_input()
      tech_file = open(filename, "r")
      break;
    except:
      print ("oops file name is not ok or not able to find the file try again ...")


# here we have to write the keyword or pattern to 
# serach which willl give us some clue
# here we need to put intellegence

pattern_list = ['I/f:',                    #this pattern is for
                'State:', 
                'Dest:',                    #this pattern is for
                '\s+diag:\s+']                    #this pattern is fora

def get_all_interface_list(tech_file):
        for line in tech_file:
            match = re.search(pattern_list[0],line)
            if (match):
                if_list.append(line)
        tech_file.seek(0)

def get_all_state_list(tech_file):
        for line in tech_file:
            match = re.search(pattern_list[1],line)
            if (match):
                state_list.append(line)
        tech_file.seek(0)

def get_all_dest_list(tech_file):
        for line in tech_file:
            match = re.search(pattern_list[2],line)
            if (match):
                dest_list.append(line)
        tech_file.seek(0)

def get_all_diag_list(tech_file):
        for line in tech_file:
            match = re.search(pattern_list[3],line)
            if (match):
                diag_list.append(line)
        tech_file.seek(0)

def show_output():
        for i in range(len(if_list)):
            if  if_list[i]:
                print (if_list[i],    end = "")
            if  ( len (state_list) > i and state_list[i]):
                print (state_list[i],end = "")
            if  ( len (dest_list)  > i and dest_list[i] ):
                print (dest_list[i], end = "")
            if  ( len (diag_list)  > i and diag_list[i] ):
                print (diag_list[i], end = "")
            print ("")


print ("++++++ file is ok here we go for hunt +++++")
print ("")

get_all_interface_list(tech_file)
get_all_state_list(tech_file)
get_all_dest_list(tech_file)
get_all_diag_list(tech_file)
show_output()

print ("++++++ End of  hunt +++++")
# Close opend file
tech_file.close()


#End of File 

