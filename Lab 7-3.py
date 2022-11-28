#1. Create a Python file named lab_7-3.py
#2. Copy your lab 7-1 code into the file
#3. Add 4 test cases to the end 
# of the file, with comments
#4. Ensure your lab runs accurately

#original
#1. Create a Python file named lab_7-1.py
#2. Create a function called greeting()
def greeting():
#3. Add a docstring to the function that explains how the function can only print "Hello World" on one line
    '''print: Hello World'''
#4. Add a statement in the function to print "Hello World!"
    x = "Hello World"
#5. Add a statement that returns the docstring for the greeting
#function
    return (x)
#6. Add another statement to call the function
print (greeting())

#Test Case #1
print(greeting() == "What's Up")
#Test Case #2
print(greeting() == "Error 101")
#Test Case #3
print(greeting() == "Hello World")
#Test Case #4
print(greeting() == "LEGO Ninjago")
