# PaperStaorage\encode\main.py
# The mainframe for encoding data

USAGE = '''
call this script in powershell, cmd or bash (in admin mode where applicable)
(Square brackets [] indicate an input field the text inside describes how it should be used)

(sudo) python main.py -p [path to folder containing files for encoding] -o [path for images to be outputted to] (-x [width of output in pixels] -y [height of output in pixels])

Can also be used with full words as below.
(sudo) python main.py --path [path to folder containing files for encoding] --outpath [path for images to be outputted to] (--width [width of output in pixels] --height [height of output in pixels])
'''

import matplotlib, sys, export

debuggers = False # Are debuggers are active? Please MANUALLY change this to False when ALL debuggers are removed and vise versa.

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
path = ".\\in\\in.zip"
outpath = ".\\out\\"
width = 400, 574

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

                if arg == "width":
                    width = args[nextArg]

                if arg == "height":
                    height = args[nextArg]

            else:
                if arg == "p":
                    path = args[nextArg]

                if arg == "o":
                    outpath = args[nextArg]

                if arg == "x":
                    width = args[nextArg]

                if arg == "y":
                    height = args[nextArg]
        currentArg += 1
        nextArg = currentArg + 1
except IndexError:
    print("ERROR: Missing argument for a tag.")
    sys.exit(0)

# DEBUG: print("path: "+path) # DEBUG
# DEBUG: print("output path: "+outpath) # DEBUG

## ACTUALLY RUNNING IT
e = export.exporter(outpath)

e.imagedimensions = (int(width), int(height))

while e.outOfData == False:
    e.makeImg(e.makeBinary(path))
