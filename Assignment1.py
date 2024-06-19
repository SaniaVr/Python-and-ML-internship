# Q1
num1=int(input("Enter the First Number:"))
num2=int(input("Enter the Second Number:"))
sum=num1+num2
print("The Sum of the two number={}\n".format(sum))

#Q2
num=int(input("Enter a Number:"))
if (num%2==0):
    print("EVEN")
else:
    print("ODD")
    
#Q3
num=int(input("Enter a Number:"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("FACTORIAL={}".format(factorial))

#Q4
name=input("Please enter your name:")
print("Good Evening {}".format(name))

#Q6
with open('your_file.txt', 'r') as file:
    content = file.read()
print(content)

#Q7
name=str(input("Enter a Word:"))
print("Length of Word:{}".format(len(name)))

#Q8
firstname=str(input("Enter your first name:"))
lastname=str(input("Enter your last name:"))
fullname=firstname + lastname
print(" Hello!! My name is {}".format(fullname))

#Q9
word=str(input("Enter a Word:"))
if "ing" in word:
    print("TRUE")
else:
    print("FALSE")

#Q10
word=str(input("Enter a Word:"))
print(word.upper())

#Q11
def generate_fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = []
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(generate_fibonacci(n))

#Q12
num=int(input("Enter a Number:"))
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10
print("Sum of digits={}".format(sum))

#Q13
yr=int(input("Enter year of Birth:"))
curryr=int(input("Enter present year:"))
age=curryr-yr
print("AGE={}".format(age))

#Q14
l=[]
while(True):
    line=input("Enter the line: ")
    if(line==''):
        break
    else:
        l.append(line)
for i in l:
    print(i)

#Q16
def count_char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
input_string = input("Enter a String:\n")
char_frequency = count_char_frequency(input_string)
print(char_frequency)

#Q17
def to_title_case(s):
    return s.title()
string = input("Enter the String:\n")
title_cased_string = to_title_case(string)
print(title_cased_string)

#Q18
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
string1 = input("Enter String1:")
string2 = input("Enter String2:")
if are_anagrams(string1, string2):
    print("TRUE")
else:
    print("FALSE")

#Q19
import string
def remove_punctuation(input_str):
    translator = str.maketrans('', '', string.punctuation)
    return input_str.translate(translator)

input_string = input("Enter a String:")
clean_string = remove_punctuation(input_string)
print(clean_string)

#Q20
l=[]
sum=0
total=int(input("Enter the total number of elements:"))
for i in range(0,total):
    elements=int(input("Enter the Element {}:".format(i+1)))
    sum=sum+elements
    l.append(elements)
print(l)
print("Sum of Elements={}".format(sum))

#Q21
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

lst = [1, 2, 3, 2, 4, 2, 5]
element = 2
occurrences = count_occurrences(lst, element)
print(f"The element {element} occurs {occurrences} times in the list.")

#Q22
'''/Write a python program that returns the 
minimum and maximum values in a list of numbers.'''
l=[]
sum=0
total=int(input("Enter the total number of elements:"))
for i in range(0,total):
    elements=int(input("Enter the Element {}:".format(i+1)))
    l.append(elements)
    maxelement=max(l)
    minelement=min(l)
print(l)
print("Maximum in List={}".format(maxelement))
print("Minimum in List={}".format(minelement))

#Q23
'''Write a program that converts temperature from Celsius to Fahrenheit
and vice versa based on user input.'''
tempFah=float(input("Enter the Temperature in Fahrenheit:"))
tempCel=float(input("Enter the Temperature in Celcius:\n"))
celcius=5.0/9.0*(tempFah-32)
Fahrenheit=(tempCel*9/5)+32
print("Temperature in Fahrenheit={}".format(Fahrenheit))
print("Temperature in Celcius ={}\n".format(celcius))

#24
'''Write a program that acts as a simple calculator. It should take two
numbers and an operator (+, -, *, /) as input and print the result.'''
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=str(input("Enter the operation:"))
if operation=='+':
    print("Sum={}".format(num1+num2))
elif operation=='-':
    if num1>num2:
        print("Difference={}".format(num1-num2))
    else:
        print("Difference={}".format(num2-num1))
elif operation=='x':
    print("Product={}".format(num1*num2))
else:
    print("Quotient={}".format(num1/num2))

#Q26
def check_string():
    string = input("Enter a string: ")
    prefix = input("Enter a prefix: ")
    suffix = input("Enter a suffix: ")

    if string.startswith(prefix):
        print(f"The string '{string}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{string}' does not start with the prefix '{prefix}'.")

    if string.endswith(suffix):
        print(f"The string '{string}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{string}' does not end with the suffix '{suffix}'.")

check_string()

#Q27
'''Write a program in python that converts 
a string into a list of its characters.'''
word=str(input("Enter a Word:"))
l=[]
for i in range(len(word)):
    l.append(word[i])
print(l)
