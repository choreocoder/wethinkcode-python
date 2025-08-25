import sys
from pathlib import Path
import pyfiglet
from tabulate import tabulate
import csv


if len(sys.argv) != 2:
    sys.exit("You must provide exactly one file")

filename = sys.argv[1]
if not filename.endswith(".csv"):
    sys.exit("File must end with .csv")

path = Path(filename)
if not path.exists():
    sys.exit("File does not exist")

with open(filename, "r") as file:
    reader = csv.reader(file)
    headers = next(reader)
    rows = list(reader)

    table = tabulate(rows, headers=headers, tablefmt="grid")
    print(table)
