import sys
import csv

# Check for correct number of command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

filein = sys.argv[1]
fileout = sys.argv[2]

# Attempt to open input file
try:
    infile = open(filein, "r")
except FileNotFoundError:
    sys.exit(f"Could not read {filein}")

# Process CSV
with infile:
    reader = csv.DictReader(infile)

    with open(fileout, "w", newline="") as outfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            full_name = row["name"]
            house = row["house"]

            # Split "Last, First" correctly
            parts = full_name.split(",")
            last = parts[0].strip()
            first = parts[1].strip()

            writer.writerow({"first": first, "last": last, "house": house})
