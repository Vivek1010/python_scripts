#!/usr/bin/env python

# __author__     = "Vivek Banger"
# __copyright__  = "Copyright 2016,"
# __credits__    = ["", "", "", ""]
# __license__    = "GPL"
# __version__    = "0.1"
# __maintainer__ = ""
# __email__      = "vbanger@cisco.com"
# __status__     = "non-Production"


import re

#global varriables
found = False;  #keep is false

# get the user input,never trust user
while(True):
    try:
      print "Enter a file name:",
      filename = raw_input()
      tech_file = open(filename, "r")
      break;
    except:
      print "oops file name is not ok or not able to find the file try again ..."


# here we have to write the keyword or pattern to 
# serach which willl give us some clue
# here we need to put intellegence

pattern_list = ['\d+VI',                    #this pattern is for
                'showtech_run', 
                'Couldn'                    #this pattern is for
                'write a pattern  here',    #this pattern is for
                'write another pattern']    #this pattern is for

print "++++++ file is ok here we go for hunt +++++"
for pattern in pattern_list:

    found = False 
    print "Hunting for >>>" + pattern
    for line in tech_file:
        match = re.search(pattern,line)
        if (match):
            print "Mach found >>>"+line
            found = True;

    if (found != True):
        print "Sorry ! Not Even a single pattern match found for >>>" + pattern 
    # 2 hour bug :P          
    tech_file.seek(0)
            

print"++++++ End of  hunt +++++"
# Close opend file
tech_file.close()


#End of File 

