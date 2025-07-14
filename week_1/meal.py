#1. Ask user for input and what the time is
#2. Convert the time that comes as a string to a floating point value
#3. Depending on what the time is, return the meal time; either breakfast, lunch or supper
def convert(time):
    hours, minutes = time.split(":")
    x = float(hours)
    y = float(minutes)
    is_denom = 60
    hours = x + (y / is_denom)
    return hours

def main():
    time = input("What is the time? ")
    hours = convert(time)

    if 7.0 <= hours <= 8.0:
        print("Breakfast Time!")
    elif 12.0 <= hours <= 13.0:
        print("Lunch Time!")
    elif 18.0 <= hours <= 19.0:
        print("Dinner Time!")
    else: pass

main()

#Biggest key: For inclusive, in the conditional, desired return must be in between and not come first.
