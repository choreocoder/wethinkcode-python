#Define speed of light
#Give Python Conversion formula
#Create input for user

speed_of_light = 300000000

def convert(weight):
    energy = weight * speed_of_light**2
    return energy

def main():
    question = (int(input("Insert your mass in Kgs " )))
    big_energy_number = convert(question)
    print(big_energy_number)


main()
