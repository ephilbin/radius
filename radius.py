def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius 
    return area #make sure variable names are same
    
radius_input = input("Enter the radius of the circle: ")


try: #use a try/except block to handle exceptions
    radius = int(radius_input)
    circle_area = calculate_area(radius)
    print("The area of the circle is:", circle_area)
except ValueError:
    print("Invalid input: radius must be an integer")
except Exception as e:
    print("An error occured:", str(e))
#The third bug would occur if the user accidentlly
#enters something other than an integer