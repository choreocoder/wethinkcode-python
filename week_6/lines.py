import sys
from pathlib import Path

#Check number of command-line arguments
if len(sys.argv) != 2:
    sys.exit("You must provide exactly one file")

#Get filename and check extension
filename = sys.argv[1]
if not filename.endswith(".py"):
    sys.exit("File must end with .py")

#Check if file exists
path = Path(filename)
if not path.exists():
    sys.exit("File does not exist")

#Count lines of code
count = 0
with open(filename, "r") as file:
    for line in file:
        stripped_line = line.strip()
        if stripped_line == "":
            continue
        elif stripped_line.startswith("#"):
            continue
        else:
            count += 1

#Print result
print(count)
