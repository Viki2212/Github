print("This is python file")
print("this update in 20.08.2022")
print("this update in 21.08.2022")
print("this update in 24.08.2022")
print("this update in 25.08.2022")
print("this update in 26.08.2022")
print("this is laptop update 03.09.22")

for row in range (6):
    for col in range (row):
        print ("*", end=" ")
    print(" ")
  
 print(100 // 3)
print(100 / 3)
print(2 * 3)
print(2 ** 3)
print(2 * 2 * 2)

print(100 % 7)
print(100 % 9)
print(100 % 2)

print(2 ** 3 + 2 * 3)
print((2 ** 3) + 2 * 3)
print((2 ** 3 + 2) * 3)

tamil = 10
tAmil = 20
taMil = 30
tamIl = 40
tamiL = 50

_tamil = 60
___tamil = 70
_tamil_ = 80

print(tamil)
print(tAmil)
print(taMil)
print(tamIl)
print(tamiL)
print(_tamil)
print(___tamil)
print(_tamil_)

result = True
print(type(result))

no = 20.4585
print(type(no))
print(id(no))
print(round(no))
print(round(no, 2))
print("----------------")
no = 0b100101
print(no)

no = 0o776
print(no)

noo = 0x456abcd
print(noo)
print("----------------")
no1 = bin(1466)
print(no1)

no2 = oct(1466)
print(no2)

no3 = hex(1466)
print(no3)

no4 = 3e3  # E, e is power of 3
print(no4)
print("----------------")
no5 = 3 + 5j
print(no5)
print(type(no5))
no6 = 10 + 6j
total = no5 + no6
print(total)
print(no5.real)
print(no5.imag)
print("----------------")

name = "varun"
print(len(name))
val = (len(name))

print(name[-val: val])
print(name[::-1])

name = 'appa'
print(name)
name1 = (name[::-1])
print(name1)
print(name == name1)
print("----------------")

values = [98, 87, 56, 45, 71]

print(values)
total = 0
for val in values:
    print(val)
    total = total + val
print(total)
print("----------------")

values = [98, 87, 56, 45, 71]
for no in values:
    if no % 2 == 0:
        print(no)
print("----------------")
for no in values:
    if not no % 2 == 0:
        print(no)

print("Hi Hello")
print("Hi\tHello")
print("Hi\nHello")
print('I\'m fine')

no = 22
no += 1
print(no)
no -= 1
print(no)
no *= 10
print(no)
no **= 1
print(no)
no /= 2
print(no)
no //= 2
print(no)
no %= 6
print(no)


def Election(age):
    if age >= 60:
        print("Welcome sir/madam, You are senior Citizen, you are eligible")
    elif age >= 18:
        print("you are eligible")
    else:
        print("you not eligible")


age = int(input("enter your age: "))

Election(age)


def fact(no):
    if no == 1:
        return 1
    return no * fact(no - 1)


print(fact(7))
# find radius
import math  # import math (or) from math import pi

radius = int(input("enter the radius: "))
ans = math.pi * radius * radius
if ans >= 200:
    print("the circle is large", math.ceil(ans))
else:
    print("the circle is small", math.ceil(ans))

calculate = input("enter: ")  # eval is change the string calculation type to int type
print(calculate)
calculate = eval(calculate)
print(calculate)

from sys import argv

print(int(argv[1]) * int(argv[2]))
print(int(argv[1]) + int(argv[2]))

# Formatted string
no1, no2, no3 = 10, 20, 30
print("no1 is %i" % no1)
print("no2 is %i" % no2)
print("no3 is %d" % no3)
print("No1 is %i and No2 is %d and No3 is %d" % (no1, no2, no3))

name = "vignesh"
print("Hi This is %s" % name)

# Replacement operator

name = "Viki"
accNo = 12345
city = "Salem Branch"

print("Hi! {0}.. Your Account Number is {1} Your From {2}..".format(name, accNo, city))
print("Hi! {a}.. Your Account Number is {b} Your From {c}..".format(a=name, b=accNo, c=city))
print("Hi! {}.. Your Account Number is {} Your From {}..".format(name, accNo, city))

# Grade Programm
mark = int(input("Enter your Mark: "))
if mark >= 90:
    print("You are 'A+' Grade")
elif mark >= 80:
    print("You are 'A' Grade")
elif mark >= 70:
    print("You are 'B+' Grade")
elif mark >= 60:
    print("You are 'B' Grade")
else:
    print("you are 'C' Grade, You Need improments")

# nest if conditions

no1 = int(input("enter the no1: "))
no2 = int(input("enter the no2: "))
no3 = int(input("enter the no3: "))

if no1 > no2 and no1 > no3:
    print("No1 big")
elif no2 > no1 and no2 > no3:
    print("No2 big")
else:
    print("No3 big")

# odd or even

no = int(input("Enter the no: "))
if no % 2 == 0:
    print("even")
else:
    print("odd")

# While loop Condition

mind = 7

while True:
    guess = int(input("Enter your guess: "))
    if guess == mind:
        print("correct")
        break
    elif guess > mind:
        print("Big")
    elif guess < mind:
        print("Small")

count = 101
while count >= 1:
    if count % 2 == 0:
        print(count)
    else:
        print(count, end=" ")
    count -= 1

# factorial program
total = 0
no = 1

max = int(input("Enter the val: "))

while no <= max:
    total = total + no
    no += 1
print(total)

no = 1
while no <= 10:
    if no == 5:
        no += 1
        continue
    print(no)
    no += 1

name = ""
while not name == "viki":
    name = input("Enter your name: ")

mail = input("enter your email: ")
length = len(mail)
i = 0
count = 0
while i < length:
    if '0' <= mail[i] <= '9':
        print(mail[i], end=" ")
        count += 1
    i += 1
print(" your count is", count)

no = 0
while no <= 20:
    if no % 2 == 0:
        print(no, end=" ")
    no += 1

choice = ''
total = 0
while not choice == 'no':
    mark = int(input("Enter your mark :"))
    total = total + mark
    choice = input("say no to stop: ")
else:
    print("Your total is: ", total)

# common divisors
import math

no1, no2 = 200, 250
print("math GCD", math.gcd(no1, no2))
div = 2

if no1 < no2:
    small = no1
else:
    small = no2
while div <= small:
    if no1 % div == 0 and no2 % div == 0:
        # print(div)
        last = div
    div += 1
else:
    print("The greatest last div: ", last)

import math

no1, no2 = 200, 300
div = 2

if no1 < no2:
    small = no1
elif no2 < no1:
    small = no2
while div < small:
    if no1 % div == 0 and no2 % div == 0:
        print(div)
        last = div
    div += 1
print("Your GCD is: ", last)
print("Math GCD is: ", math.gcd(no1, no2))

no1, no2 = 7, 43
big = no1 if no1 > no2 else no2

while True:
    if big % no1 == 0 and big % no2 == 0:
        print(big)
        break
    big += 1

# prime or not prime
no = int(input("Enter your number: "))
div = 2

while div < no:
    if no % div == 0:
        print("This number divised by: ", div, " not prime")
        break
    div += 1
else:
    print(div, "is prime number")

# Fibonacci Method

first = 0
second = 1
count = 1
print(first)
print(second)

while count <= 8:
    third = first + second
    print(third)
    first = second
    second = third
    count += 1

# Fibonacci Method-2
first = -1
second = 1

while True:
    print(first + second)
    second = first + second
    first = second - first
    if second == 2584:
        break

# palindrome
no = int(input("Enter your value: "))
count = 0
total = 0
same = no

while no > 0:
    total = (total * 10) + no % 10
    no = no // 10
    count += 1
else:
    print("Count of digits: ", count)
    print("Revers of digits: ", total)
    if same == total:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Armstrong number

no = int(input("Enter your number: "))
same = no
total = 0

while no > 0:
    dig = no % 10
    digPower = dig * dig * dig
    total = total + digPower
    no = no // 10
else:
    if same == total:
        print("Armstrong")
    else:
        print("Not Armstrong")

# Armstrong number-2

no = int(input("Enter your number: "))
same = no
total = 0

while no > 0:
    dig = no % 10
    digPower = dig ** 3
    total = total + digPower
    print(total)
    no = no // 10
else:
    if same == total:
        print("Arms")
    else:
        print("Not Arms")

# Binary value find
no = 5
binary = ''

while no > 0:
    val = no % 2
    binary = str(val) + binary
    no = no // 2
else:
    print(binary)
    print(type(binary))

# for loop
name = input("enter your email: ")
count = 0

for i in name:
    if 'a' <= i <= 'z':
        count += 1
        print(i, end=" ")
else:
    print("letter count is: ", count)

# for loop words indentify
name = input("enter your email: ")
count = 0

for i in name:
    if i == ' ':
        count += 1
else:
    print("letter count is: ", count + 1)

# for loop with range
for num in range(6):
    print(num, end=" ")
print()

for num in range(1, 6):
    print(num, end=" ")
print()

for num in range(1, 6, 2):
    print(num, end=" ")
print()

for num in range(10, -1, -2):
    print(num, end=" ")
print()

no = 1
for num in range(3, 33, 3):
    print(no, "* 3 = ", num)
    no += 1

# While Factorial
no = 1
fact = 1

while no <= 6:
    fact = fact * no
    no += 1
else:
    print(fact)

# for Factorial

no = 6
facto = 1

for i in range(1, no + 1):
    facto = facto * i
else:
    print(facto)

word = 'abcd'

for i in range(len(word) - 1, -1, -1):
    print(word[i])

word = 'abcd'
word1 = word[::-1]
print(word1)

# Pattern program

for i in range(5):
    print("* " * 5)

no1 = 1
while no1 <= 5:
    for no in range(5):
        print(no1, end=" ")
    print()
    no1 += 1

# no Pattern program

for row in range(1, 11):
    for col in range(1, 4):
        print(row * col, end="  ")
    print()

# num Pattern program

for row in range(6, 1, -1):
    for col in range(1, row):
        print(col, end=" ")
    print()

# num Pattern program
row = 6
while row > 0:
    for col in range(1, row):
        print(col, end=" ")
    print()
    row -= 1

for row in range(1, 6):
    for col in range(row, 6):
        print(row, end=" ")
    print()

# num Pattern program
row = 5
no = 1
while row > 0:
    for col in range(row):
        print(no, end=" ")
    print()
    row -= 1
    no += 1

for row in range(1, 6):
    for col in range(row):
        print(row, end=" ")
    print()
    row -= 1

row = 5
no = 1
for row in range(10, 0, -1):
    for col in range(row):
        print(no, end=" ")
    print()
    no += 1

# num Pattern program
col = 5
for row in range(1, 6):
    for col in range(col):
        print(row, end=" ")
    print()
    row -= 1

print()

no = 1
for row in range(5, 0, -1):
    for col in range(row):
        print(no, end=" ")
    print()
    no += 1

# Word patterns

name = "Vignesh"
count = len(name)

while count > 0:
    for col in range(count):
        print(name[col], end=" ")
    print()
    count -= 1

# Word patterns
name = "Vignesh"
count = len(name)

for row in range(count, 0, -1):
    for col in range(row):
        print(name[col], end=" ")
    print("")

# Word patterns

for row in range(1, 6):
    for col in range(row):
        print("*", end=" ")
    print()

print("-------------------------------------")

row1 = 1
while row1 <= 5:
    for col1 in range(row1):
        print("*", end=" ")
    print()
    row1 += 1

for col in range(6):
    print(" " * (5 - col), "*" * col, end=" ")
    print()

s = "i am viki"
for i in s[::-1]:
    print(i, end=" ")

s = "i am viki"
count = len(s) - 1

while count >= 0:
    print(s[count], end=" ")
    count -= 1

# membership operators in/not in

name = "Vignesh"
print('i' in name)
print("i" not in name)

# membership operators in/not in

sen = input("Enter the sentence: ")
word = input("Enter the word your search: ")

if word in sen:
    print("Present")
else:
    print("Not Present")

# string comparision

name = input("Enter sen 1: ")
name1 = input("Enter sen 2: ")

if name == name1:
    print("Same")
elif name > name1:
    print("name1")
else:
    print("name2")

# space removal in a given string
sent = input("enter your sent: ")
print("Before count", len(sent))
sent = sent.strip()
print("After count", len(sent))

# finding words
word = "python java scala javascript"
print(word)
print()
print(word.find("java"))
print(word.index("java"))
print(word.find("c++"))
print(word.index("c++"))  # ValueError
print(word.rfind("scala"))
print(word.find("scala", 0, 18))

# finding words
word = input("enter the word: ")
alpha = input("enter your alpha: ")
count = len(word)
index = 0
total = 0
while True:
    index = word.find(alpha, index, count)
    if index == -1:
        break
    print("total count is", index)
    total += 1
    index += 1
print()
print("total alpha is: ", total)

# finding words
word = input("enter the word: ")
alpha = input("enter your albha: ")
print(word.count(alpha))
print(word.count(alpha, 0, 3))

# finding words
word = "sunday is not holiday he is not killer she is not teacher"
alpha = 'not'
count = len(word)
index = -1
coun = 0
while not coun == 2:
    index = word.find(alpha, index + 1, count)
    if index == -1:
        break
    print("total count is", index)
    coun += 1
print()
print("total alpha is: ", index)
print(word[:index], 'our', word[index + 3:])

state = "india"
print(state[0].upper() + state[1:])
print(state[:-1] + state[-1].upper())

# Capitalize the characters
word = input("Enter your word: ")
length = len(word)

for i in range(length):
    if 'a' <= word[i] <= 'z':
        print(chr(ord(word[i]) - 32), end=" ")
    elif 'A' <= word[i] <= 'Z':
        print(chr(ord(word[i]) + 32), end=" ")
    else:
        print(word[i], end=" ")

# Capitalize the characters
word = 'tamil nadu india'
print(word[0].upper() + word[1:])

# find odd / even characters
name = 'rajarajachozhan'
i = 0

while i < (len(name)):
    print(name[i], end=" ")
    i += 1
print()
for i in range(len(name)):
    print(name[i], end=" ")
print()
print(name[::2])
print()
print(name[1::2])

# Merging charecters

s1 = 'Vgeh'
s2 = 'ins'

small = len(s1) if len(s1)<len(s2) else len(s2)
i = 0
output = ''
while i < small:
    output = output + s1[i] + s2[i]
    i += 1
else:
    output = output + s1[-1]
    print(output)

# Merging charecters

s1 = 'Vgeh'
s2 = 'ins'

small = len(s1) if len(s1)<len(s2) else len(s2)
output = ''

for i in range(small):
    output = output + s1[i] + s2[i]
else:
    output = output + s1[-1]
    print(output)

# Seperate the alpha and numeric
name = 'a1b2c3'
i = 0

while i < len(name):
    if 'a' <= name[i] <= 'z':
        print(name[i], end='')
    i += 1

# Seperate the alpha and numeric
name = 'a1b2c3d4e5f6g7h8i9j0'
alpha = ''
num = ''

for i in name:
    if i.isalpha():
        alpha = alpha + i
    else:
        num = num + i
else:
    print(alpha+num)

# Seperate the alpha and numeric
name = 'a3'

for i in name:
    print(name[0]+chr(ord(name[0])+3))

# Seperate the alpha and numeric
name = 'a3'
output = ''

for i in name:
    if i.isalpha():
        output = output + i
        let = i
    else:
        output = output + (chr(ord(let)+ int(i)))
else:
    print(output)

# value Assignment
name = 'Viki'
age = 29

print('my name is',name, 'and my age is', age)
print('my name is {} and my age is {}'.format(name, age))
print('my name is {0} and my age is {1}'.format(name, age)) #must starts with 0
print('my name is {p} and my age is {q}'.format(p=name, q=age))
print('my name is {q} and my age is {p}'.format(p=name, q=age))
print('my age is {:d}'.format(345))
print('my mark is {:3.2f}'.format(345.55550))


