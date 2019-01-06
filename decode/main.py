# PaperStorage\decode\main.py
# mainframe for decoding images

import sys

USAGE = '''
call this script in powershell, cmd or bash (in admin mode where applicable)
(Square brackets [] indicate an input field the text inside describes how it should be used)

(sudo) python main.py -p [path to folder containing files for decoding] -o [path for .zip file to be outputted to]

Can also be used with full words as below.
(sudo) python main.py --path [path to folder containing files for decoding] --outpath [path for .zip file to be outputted to]
'''

import matplotlib, sys, fileHandler

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

# DECODE ARGS
args = sys.argv
# DEBUG: print(args)
currentArg = 0
nextArg = currentArg + 1
path = None
outpath = None
try:
    for arg in args:
        # DEBUG: print("current arg is {} at position {}".format(arg, currentArg)) # DEBUG
        # DEBUG: print(args) # DEBUG
        if arg[0] == "-": # Checks for a tack in the first position for tags
            arg = _delchar(arg, 0) # Removes the tag from the arg
            # DEBUG: print(arg)
            if arg[0] == "-": # Checks for a tack in the second position of string for whole word tags
                arg = _delchar(arg, 0)
                # DEBUG: print(arg)

                if arg == "path":
                    path = args[nextArg]

                if arg == "outpath":
                    outpath = args[nextArg]
            else:
                if arg == "p":
                    path = args[nextArg]

                if arg == "o":
                    outpath = args[nextArg]
        currentArg += 1
        nextArg = currentArg + 1
    if outpath == None or path == None:
        raise IndexError # This isn't ideal but I don't want the program continueing if there missing args
except IndexError:
    print("ERROR: Missing argument for a tag.")
    sys.exit(0)

print("path: "+path) # DEBUG
print("output path: "+outpath) # DEBUG
