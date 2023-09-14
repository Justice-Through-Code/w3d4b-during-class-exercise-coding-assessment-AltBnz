#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    
    # User Options
    Circle = 1
    Rectangle = 2
    Triangle = 3
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print(Circle + ' ' + Rectangle + ' ' + Triangle)

    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input('Select a shape by entering 1, 2, or 3')
    # TODO: Convert the variable 'choice' to an integer data type.
    choice = int(choice)

    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    
    if choice == 1: #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle

        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        radius = input('What is the radius of a circle: ')
        # TODO: Convert 'radius' to float.
        radius = float(radius)
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        area = circle_pi * radius ** 2
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared. 
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        length = input('What is the length of the rectangle? ')
        width = input('What is the width of the rectangle? ')
        # TODO: Convert both 'length' and 'width' to float.
        length = float(length)
        width = float(width)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        area = length * width
        # HINT: The formula to find the area of a rectangle: length times width

    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        base = input('What is the base length of the triangle? ')
        height = input('What is the base height of the triangle? ')
        # TODO: Convert both 'base' and 'height' to float.
        base = float(base)
        height = float(height)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        area = base * height / 2
        # HINT: The formula to find the area of a Triangle: half times base times height

    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
    
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
    print(f'First we assigned values to the global variables "Circle", "Rectangle", and "Triangle".\n Next, we printed a single string\
         (with with our three options of shapes for the user to calculate the area of. The user is asked to enter a number which corresponds with one of\
         (the three shapes. This number, I converted to an integer. Then, conditional if-elif-else statements followed.\
         (If the user chose the number 1, the area of a circle is calculated. If the user chose the number 2, the area of a rectangle is calculated.\
         (If the user chose the number 3, the area of a rectangle is calculated. In each of the conditional statements, one or more values\
         (was converted to floats using the float conversion function. If the user entered anything other than  '

if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
