# CSV handler.py
import csv, sys

USAGE = '''
call this script in powershell, cmd or bash (in admin mode where applicable)
(Square brackets [] indicate an input field the text inside describes how it should be used)

(sudo) python(3) CSVsorter.py -f [file containing unsorted results] -o [file for sorted results to be outputted to]

Can also be used with full words as below.
(sudo) python(3) CSVsorter.py --file [file containing unsorted results] --outfile [file for sorted results to be outputted to]
'''

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
        # DEBUG: print(item[0]) # DEBUG
        item[0] = float(item[0])
    # DEBUG: print(sorted(table)[::-1]) # DEBUG

with open(outfile, "w+") as f:
    writer = csv.writer(f, delimiter=',')
    for line in table:
        writer.writerow(line)
