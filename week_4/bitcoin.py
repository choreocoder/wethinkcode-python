import sys #Imports sys moddule where I will use the command-line
import requests #Imports request mmodule so I use API & fetch data from servers

# Ensure the user gives exactly one command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Try to convert the argument to a float
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Try to fetch the Bitcoin price
try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin",
        headers={
            "Authorization": "Bearer YourActualApiKeyHere" #Shows server that I am authorized
        }
    )
    response.raise_for_status() #Shows me how server is responding to my reuqest
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Network error. Try again later.")

# Calculate the total cost
total_cost = bitcoins * price
print(f"${total_cost:,.4f}")
