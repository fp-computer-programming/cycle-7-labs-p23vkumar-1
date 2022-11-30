#1. Create a Python file named lab_7-8.py
#2. Create a 2 separate functions within the same document.
#3. Create a 3rd function which requires both the first two functions
#within it
#4. Create 4 test cases for your 3rd function.

#create a function for subtraction
def subtract(Integer1, Integer2):
    '''Subtract a Number''' #subtract a number
    new_subtract = Integer1 - Integer2 #subtract two integers within parameters
    return new_subtract #return variable with two variable within parameters
print(subtract(22, 23)) #subtract by pritning functiopn
#create a function to divide 
def divide(Integer1, Integer2):
    #divide a number
    '''divide a Number'''
    #create a new variable to divide the two variables within the function
    new_divide = Integer1 / Integer2
    #return the new variable
    return new_divide
#print division of two numbers
print(divide(81, 99))

#create a new function to subtract and divide
def combinationOfStructionAndDivide(Integer1, Integer2):
    #subtract a number
    '''subtract a number'''
    #divide a number
    '''divide a number'''
    #subtract two numbers from subtraction function
    subtract_update = subtract(Integer1, Integer2)
    #divide two numbers from division function
    divide_update = divide(Integer1, Integer2)
    #return combinnation of subtraction and division
    return subtract_update and divide_update
#print the overall function
print(combinationOfStructionAndDivide(1, 2))

#Test Case 1 for third function
print(combinationOfStructionAndDivide(22, 22))
#Test Case 2 for third function
print(combinationOfStructionAndDivide(54, 235))
#Test Case 3 for third function
print(combinationOfStructionAndDivide(88, 9))
#Test Case 4 for third function
print(combinationOfStructionAndDivide(2345, 3.14152986252234634))
