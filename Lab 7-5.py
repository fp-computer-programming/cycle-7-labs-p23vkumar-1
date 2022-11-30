#1. Create a Python file named lab_7-5.py
#2. Copy the code from your labs 6-5 through 6-8 
# 3. Turn each of the programs into a function
#4. Add 4 test cases to the functions
#5. Ensure your code runs accurately

#6-5
#1. Create a Python file named lab_6-5
#2. Create a program that will take a list (of numbers) of any length and return the highest and lowest value in the list. If the list does not have at least 2 unique numbers, return the string: “error: list does not meet specifications”)

#create a list
x_L_I_S_T = [16, 100, 20, 56, 76]

#print List 
print(x_L_I_S_T)

#reverse list if needed 
x_L_I_S_T.sort (reverse = True)
#print reversed list
print(x_L_I_S_T)

#length of list has to be greater than 2
if len(x_L_I_S_T) > 2:
    #print(higher number)
    print(x_L_I_S_T[0])
    #print(lower number)
    print(x_L_I_S_T[-1])
    #another if conditions for higher not equal to lower
    if x_L_I_S_T[0] != x_L_I_S_T[-1]:
        #print expression to meet command
        print("Meets Speciications")
#otherwise redo it
else:
    print("Error! List Does Not Meet Specifications")

#----------------------------------------------------------------------------------------------------------------------------------
#6-5 Code converted to a function
#
def NUMBEREDLIST(input1,input2,input3):
    #List of numbers
    NUMBEREDLIST = [input1,input2,input3]
    #sort list to create range from low to high numbers
    NUMBEREDLIST.sort()
    return("Based on your readings, the lowest number is equal t0 "+str(NUMBEREDLIST[0])+",. The Highest number according to these readings is "+str(NUMBEREDLIST[len(NUMBEREDLIST)-1])+". Thank you for your help")

#Test case 1 for 6-5
print(NUMBEREDLIST(11,12,10))
#Test case 2 for 6-5
print(NUMBEREDLIST(15,30,2))
#Test case 3 for 6-5
print(NUMBEREDLIST(81,56,3567))
#Test case 4 for 6-5
print(NUMBEREDLIST(.23461,.7512269,.007809876543211))


#6-6

#1. Create a Python file named lab_6-6
#2. Create a program that asks a user to input 5 unique words.

word_1 = input("Enter Word: ")
word_2 = input("Enter Word: ")
word_3 = input("Enter Word: ")
word_4 = input("Enter Word: ")
word_5 = input("Enter Word: ")

#3. Construct a list of the 5 input values, in the order that the user gave them.

W_O_R_D_L_I_S_T = [word_1, word_2, word_3, word_4, word_5]

#4. Have the program display a list where each index corresponds to the length of the word given by the user at the corresponding index.

length1 = len(word_1)
length2 = len(word_2)
length3 = len(word_1)
length4 = len(word_2)
length5 = len(word_1)
L_E_N_G_T_H_L_I_S_T = [length1, length2, length3, length4, length5]
print(L_E_N_G_T_H_L_I_S_T)

#• You may assume accurate input values. NO LOOPS

#----------------------------------------------------------------------------------------------------------------------------------
#6-6 Code converted to a function

def string_of_words(x1,x2,x3,x4,x5):
    words_from_string = [x1,x2,x3,x4,x5]
    lengths_words_from_string = [len(x1),len(x2),len(x3),len(x4),len(x5)]
    return(words_from_string, lengths_words_from_string)

#Test Case 1 for 6-6
print(string_of_words("Man","of","Steel","equals","GOATED"))
#Test Case 2 for 6-6
print(string_of_words("Avengers","and","MCU","are","horrible"))
#Test Case 3 for 6-6
print(string_of_words("Novak","Djokovic","is","the","Greatest"))
#Test Case 4 for 6-6
print(string_of_words("I","Want","To","Major in","Computer Science"))

#6-7

#1. Create a Python file named lab_6-7
#2. Create a program that asks a user to input 3 numeric values

#create input variables for all of them
Number1 = int(input("Enter Number: "))
#create input variables for all of them
Number2 = int(input("Enter Number: "))
#create input variables for all of them
Number3 = int(input("Enter Number: "))

#3. Construct a list of the 3 input values, in the order that the user gave them.

#create a list of the numbered vlaues
N_U_M_B_E_R_L_I_S_T = [Number1, Number2, Number3]

#4. Have the program display a list with each of the values as integers that have been doubled

#create revised list to double to numbers
N_U_M_B_E_R_L_I_S_T_2_0 = [Number1 * 2, Number2 * 2, Number3 * 2] 
#print Numbered List
print(N_U_M_B_E_R_L_I_S_T_2_0)

#• You may assume accurate input values.

#----------------------------------------------------------------------------------------------------------------------------------
#6-7 Code converted to a function

def N_U_M_B_E_R_L_I_S_T(Number1,Number2,Number3):
    List_Of_Numbers = [int(Number1)*2,int(Number2)*2,int(Number3)*2]
    return(List_Of_Numbers)

#Test Case 1
print(N_U_M_B_E_R_L_I_S_T(1,2,3))
#Test Case 2
print(N_U_M_B_E_R_L_I_S_T(4,2345667,123456789))
#Test Case 3
print(N_U_M_B_E_R_L_I_S_T(9,23456,111))
#Test Case 4
print(N_U_M_B_E_R_L_I_S_T(16,-85430,-1111111))

#----------------------------------------------------------------------------------------------------------------------------------
#6-8

#1. Create a Python file named lab_6-8
#2. Create a program that asks a user to input 3 numeric values

#create input variables for all of them
Num1 = input("Enter Number: ")
#create input variables for all of them
Num2 = input("Enter Number: ")
#create input variables for all of them
Num3 = input("Enter Number: ")

#3. Construct a list of the 3 input values, in the order that the user gave them

#create a list of the numbered vlaues
N_U_M_B_E_R_L_I_S_T = [Num1, Num2, Num3]

#4. Have the program display the string “even” if all numbers in the list are even.

#create input variables for all of them
Number1 = int(Num1)
#create input variables for all of them
Number2 = int(Num2)
#create input variables for all of them
Number3 = int(Num3)

if Number1%2 == 0 and Number2%2 == 0 and Number3%2 == 0:
    print("List of Numbers is Even")
elif Number1%2 != 0 and Number2%2 != 0 and Number3%2 != 0:
    print("List of numbers is odd")
else:
    print("List of numbers is Mixed")
#5. Have the program display the string “odd” if all numbers in the list are odd.
#6. Have the program display the string “mixed” if the numbers in the list are both even and odd.
#• You may assume accurate input values. You may NOT use a loop.

#----------------------------------------------------------------------------------------------------------------------------------
#6-8 Code converted to a function

#create function for numbers within range of original lab
def ListNumbersWithinRange(Num1,Num2,Num3):
    #create a lst of numbers
    x_list = [int(Num1),int(Num2),int(Num3)]
    if x_list%2 == 0 and x_list%2 == 0 and x_list%2 == 0:
        print("List of Numbers is Even")
    elif x_list%2 != 0 and x_list%2 != 0 and x_list%2 != 0:
        print("List of numbers is odd")
    else:
        print("List of numbers is Mixed")

#Test Cases 1
print(ListNumbersWithinRange(1,2,8))
#Test case 2
print(ListNumbersWithinRange(2,10,6))
#Test Case 3
print(ListNumbersWithinRange(3,2345789,12346))
#Test Case 4
print(ListNumbersWithinRange(3,6,9))