import matplotlib
import sys

debugers = True # Are debuggers are active? Please MANUALLY change this to False when ALL debuggers are removed and vise versa.

if debuggers:
    print("Debuggers are active.")

def _delchar(string, charPos):
    # Deletes a character of a string
    string = list(string)
    del string[charPos]
    return str(string)


def path(pathName):
    # TODO: activate seperate file
    print("path is {}".format(pathName)) # DEBUG


args = sys.argv
# DEBUG: print(args)
currentArg = 0
try:
    for arg in args:
        print("current arg is {} at position {}".format(arg, currentArg)) # DEBUG
        if arg[0] == "-": # Checks for a tack in the first position for tags
            arg = _delchar(arg, 0) # Removes the tag from the arg

            if arg[0] == "-": # Checks for a tack in the second position of string for whole word tags
                arg = _delchar(arg, 0)

                if arg == "path":
                    path(arg[currentArg+1])

                if arg == "outpath":
                    pass
            else:
                if arg == "p":
                    path(arg[currentarg+1])

                if arg == "o":
                    pass
        currentArg += 1

except IndexError as e:
    print("IGNORING ERROR: Missing arg for a tag."+str(e))
