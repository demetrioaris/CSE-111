import math
from datetime import datetime

# Function to calculate tire volume
def calculate_volume(width, aspect_ratio, diameter):
    return (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Function to determine tire price
def calculate_price(width, aspect_ratio, diameter):
    if width == 185 and aspect_ratio == 65 and diameter == 14: # 185/65R14
        return 70.00
    elif width == 205 and aspect_ratio == 70 and diameter == 15: # 205/70R15
        return 90.00
    elif width == 215 and aspect_ratio == 55 and diameter == 16: # 215/55R16
        return 110.00
    elif width == 225 and aspect_ratio == 50 and diameter == 17: # 225/50R17
        return 130.00
    elif width == 235 and aspect_ratio == 65 and diameter == 18: # 235/65R18
        return 150.00
    else:
        return 0.0

# Main function for tire volume calculation and buying process
def tire_volume():
    print(f"Welcome to the Tire Volume Calculator and price")
    print(f"Common tire sizes are 185/65R14, 205/70R15, 215/55R16, 225/50R17, 235/65R18\n")
    
    # Get user input for tire dimensions
    width = int(input("Enter the width of the tire in mm (ex 185 - 235): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 50 - 70): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 14 - 18): "))
    
    # Calculate tire volume
    volume = calculate_volume(width, aspect_ratio, diameter)
    
    # Display the volume
    print(f"The approximate volume is {volume:.2f} liters\n")
    
    # Calculate tire price
    price = calculate_price(width, aspect_ratio, diameter)
    
    # Display the tire price
    if price > 0:
        print(f"The price for the tire of size {width}/{aspect_ratio}R{diameter} is ${price:.2f}")
    else:
        print(f"Sorry, we do not have a price for the tire of size {width}/{aspect_ratio}R{diameter}")
    
    # ask if the user wants to buy tires
    answer = input("\nDo you want to buy tires with these dimensions? (yes/no): ").strip().lower()
    
    if answer == "yes":
        print("Great! Let's get started.")
        customer_name = input("Please enter your name: ")
        phone_number = input("Please enter your phone number: ")
        
        # get the current date
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # open data to volumes.txt
        with open("volume.txt", "a") as file:
            file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {customer_name}, {phone_number}, {price}\n")
        
        print(f"Thank you, {customer_name}! Your phone number {phone_number} has been recorded.")
    else:
        print("Thank you for using our tire volume calculator.")

tire_volume()
