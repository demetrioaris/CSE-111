"""
Program: heart_rate.py
Author: [Your Name]
This program computes the slowest and fastest rates necessary to strengthen a person's heart based on their age.
"""

# Define the main function
#def main():
# Get the user's age
age = int(input("Enter your age: "))
    
# Compute the maximum heart rate
max_heart_rate = 220 - age
    
# Compute the slowest and fastest rates
slowest = int(0.65 * max_heart_rate)
fastest = int(0.85 * max_heart_rate)
    
    # Display the results
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {slowest:.0f} and {fastest:.0f}")
print("beats per minute.")

# Call the main function
#if __name__ == "__main__":
#    main()