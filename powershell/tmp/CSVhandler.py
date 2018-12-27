# CSV handler.py
import csv, sys

args = sys.argv

currentArg = 0
nextArg = 1
try:
    for arg in args:
        if arg in ["-f", "--file"]:
            file = args[nextArg]
        elif arg in ["-o", "--outfile"]:
            outfile = args[nextArg]
        currentArg += 1
        nextArg = currentArg + 1
except IndexError:
    print("IGNORING: missing argument(s)")


with open(file, "r") as f: # CSV is in format filename%size
    reader = csv.reader(f, delimiter="%")
    table = []
    for row in reader:
        table.append(row[::-1]) # The [::-1] reverses the list
    for item in table:
        item[0] = float(item[0])
    print(sorted(table)[::-1]) # DEBUG

with open(outfile, "w+") as f:
    for line in table:
        f.write(line)
