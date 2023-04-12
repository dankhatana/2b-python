import math

while True:
    # Take user input for diameter
    diameter = float(input("Enter the diameter of the circle (or enter 'q' to quit): "))
    
    if diameter == 'q':
        # If user enters 'q', exit the loop and terminate the program
        print("Exiting...")
        break
    
    # Calculate radius, area, and circumference
    radius = diameter / 2
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    
    # Print the results
    print("Radius = {:.2f}".format(radius))
    print("Area = {:.2f}".format(area))
    print("Circumference = {:.2f}".format(circumference))