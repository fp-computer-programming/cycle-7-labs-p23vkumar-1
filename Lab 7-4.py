#1. Create a Python file named lab_7-4.py
#2. Copy your lab 7-2 code into the file
#3. Add 4 test cases to the end of the file, with comments 
#4. Ensure your lab runs accurately

#original
#1. Create a Python file named lab_7-2.py
#2. Create a function called find_sum()
#3. Add the parameters num1 and num2 to the definition of find_sum()
def find_sum(num1, num2):
#4. Add statements to the function that adds the arguments passed to num1 and num2 and 
#stores them in a new variable num_sum
    num_sum = num1 + num2
    return num_sum #Finish the function with a statement that returns num_sum

#6. Create a statement that calls the function to find the sum of 111 and 222. Set it
#equal to the variable my_sum
my_sum = find_sum(111, 222)
#7. Add another print statement after the previous statement that prints my_sum
print(my_sum)

#8. What happens when you run the program?

print("After I run the program, the value of 333 is printed")

#Test 1
print(find_sum(222222222222222222222222222,1.12357884))
#Test 2
print(find_sum(83.7283,-1234))
#Test 3
print(find_sum(122345,-1))
#Test 4
print(find_sum(23456789098765432,-457806.123467073))