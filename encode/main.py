# PaperStaorage\encode\main.py
# The mainframe for encoding data

usage = '''
call this script in powershell, cmd or bash (in admin mode where applicable)
(Square brackets [] indicate an input field the text inside describes how it should be used)

(sudo) python main.py -p [path to folder containing files for encoding] -o [path for images to be outputted to]

Can also be used with full words as below.
(sudo) python main.py --path [path to folder containing files for encoding] --outpath [path for images to be outputted to]
'''

import matplotlib, sys, export

debuggers = True # Are debuggers are active? Please MANUALLY change this to False when ALL debuggers are removed and vise versa.

if debuggers:
    print("INFO: Debuggers are active.\n-----")

# GENERAL FUNCTIONS
def _delchar(string, charPos):
    # Deletes a character of a string
    # DEBUG: print(string)
    string = list(string)
    del string[charPos]
    string = "".join(string)
    # DEBUG: print(string)
    return string

# FUNCTIONS TO ACTIVATE OTHER SCRIPTS
def path(pathName):
    # TODO: activate seperate file
    print("path is {}".format(pathName)) # DEBUG

# DECODE ARGS
args = sys.argv
# DEBUG: print(args)
currentArg = 0
nextArg = currentArg + 1
try:
    for arg in args:
        # DEBUG: print("current arg is {} at position {}".format(arg, currentArg)) # DEBUG
        #print(args)
        if arg[0] == "-": # Checks for a tack in the first position for tags
            arg = _delchar(arg, 0) # Removes the tag from the arg
            # DEBUG: print(arg)
            if arg[0] == "-": # Checks for a tack in the second position of string for whole word tags
                arg = _delchar(arg, 0)
                # DEBUG: print(arg)

                if arg == "path":
                    path(args[nextArg])

                if arg == "outpath":
                    pass
            else:
                if arg == "p":
                    path(args[nextArg])

                if arg == "o":
                    pass
        currentArg += 1
        nextArg = currentArg + 1

except ValueError:
    print("IGNORING ValueError")
#except IndexError as e:
#    print("IGNORING ERROR: Missing arg for a tag."+str(e))
