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
    print('Circle' + ' ' + '=' + ' ' + '1' + ' ' + 'Rectangle' + ' ' + '=' + ' ' + '2' + ' ' + 'Triangle' + ' ' + '=' + ' ' + '3')

    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input('Select a shape by entering 1, 2, or 3: ')
    # TODO: Convert the variable 'choice' to an integer data type.
    choice = int(choice)

    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.
    choice == int(choice)
    print(choice == int(choice))
    # If converted correctly, the output in Terminal should read 'True'.
    
    if choice == 1: # Do not remove IF
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
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice .
        print('Invalid choice .')
    
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific.
    print('The first step required in the process of finding, completing, and submitting my technical assignments is to nagivagate\n')
    ('to Canvas and the Modules link in the navigation pane. Click the Overview for that week to find the assignment link.\n')
    ('Clicking the Exercise link will take you to GitHub Classroom, where you must accept the assignment. You may have to refresh\n')
    ('the page to see that your repository has been created. Click on the URL to your GitHub repository to access your assignment.\n')
    ('In GitHub, copy the URL to your repository to your clipboard. Next, launch VS Code and open a new terminal. In the terminal,\n')
    ('navigate to the parent folder of that stores your repo subfolders. Copy the remote repository to your local computer\n')
    ('by using the command "git clone". Carefullu read and understand the README file, then follow the instructions in the assignment.')
    ('Once you are satisfied that your code meets all the requirements of the assignment, run the unit test module: "python3 -m"\n')
    ('unittest. If the code fails, review your code and the output from the unit test to find the errors in your code. If the code passes,\n')
    ('take a screenshot and save it to a location from which it can be easily retrieved later. Use the commands "git add," "git commit,"\n')
    ('and "git push" to move your code from your local repository to the GitHub repo. Look for the green check mark in the GitHub repo.\n')
    ('Once you receive the green check mark, return to Canvas to turn in your assignment. Upon completing the assignment,\n')
    ('click "Start Assignment" to submit the URL to your repo in a labled text box in the lower center portion of the screen.\n')
    ('Click the submit button to submit the assignment. On the upper right side of the submission window is a "Comments" box\n')
    ('for submitting comments and attaching files. Use this feature to attach the image of your successful unit test.\n')
    ('Submit the image file and the submission is complete. Congratulations!')

if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
