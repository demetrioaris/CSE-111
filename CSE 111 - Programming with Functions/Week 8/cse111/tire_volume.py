import math
from datetime import datetime

def tire_volumen():

    #have pi
    print(f"Welcome to the Tire Volume Calculator and prices tires")
    print(f"Commun tires sizes are 185/50R14, 205/60R15, 215/55R16, 225/50R17, 235/65R18")
    print(f" ")
    # get w = width in mm
    w = int(input("Enter the width of the tire in mm (ex 185 - 235 ): "))

    # get a = aspect ratio of the tire
    a = int(input("Enter the aspect ratio of the tire (ex 50 - 70): "))

    # get d = diameter of the wheel in inche
    d = int(input("Enter the diameter of the wheel in inches (ex 14 - 18): "))

    #
    # get v = volumen of the tire
    #
    v = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000

    # Display the results
    print(f"The approximate volume is {v:.2f} liters")

    # W01 Prove Assignment: Tire Volume

    # rim diameter and tire sizes

    if w == 185 and a == 50 and d == 14: # 185/50R14
        price = 70.00
    elif w == 205 and a == 60 and d == 15: # 205/60R15
        price = 90.00
    elif w == 215 and a == 55 and d == 16: # 215/55R16
        price = 110.00
    elif w == 225 and a == 50 and d == 17: # 225/50R17
        price = 130.00
    elif w == 235 and a == 65 and d == 18: # 235/65R18
        price = 150.00
    else:
        print(f"Sorry, we do not have a price for the tire of size {w}/{a}R{d}")
        return

    # Display the tire price
    print(f"The price for the tire of size {w}/{a}R{d} is ${price:.2f}")
    
    # ask the user if she wants to buy tires with the dimensions
    answer = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()
    
    if answer == "yes":
        print("Great! Let's get started.")
        customer_name = input("Please enter your name: ")
        phone_number = input("Please enter your phone number: ")
        # get the current date
        current_date = datetime.now().strftime("%Y-%m-%d")

        # open the volumes.txt file for appending
        with open("volumes.txt", "a") as file:
            file.write(f"{current_date}, {w}, {a}, {d}, {v:.2f}, {customer_name}, {phone_number}\n")
        
        print(f"Thank you! Your personal information has been recorded.")
    else:
        print("Thank you for using our tire volume calculator and prices tires.")

tire_volumen()

