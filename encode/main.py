import matplotlib
import sys

def path(pathName):
    print("path is {}".format(pathName))


args = sys.argv
print(args)
currentArg = 0
for arg in args:
    print("current arg is {} at position {}".format(arg, currentArg))
    if arg[0] == "-":
        #Checks for a tack in the first position for tags
        arg = list(arg)
        
        if arg[1] == "-":
            #Checks for a tack in the second position of string for whole word tags


            if arg == "path":
                path(arg[currentArg+1])
        if arg == "p":
            path(arg[currentarg+1])
    currentArg += 1
