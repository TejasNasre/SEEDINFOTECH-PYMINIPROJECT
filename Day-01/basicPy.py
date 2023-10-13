#print hello wolrd in Py - Our First Py Program

print('hello wolrd')

# variable In Py

a = 5
print(a)

#Take Input frpm User

enterNum = input('enter num: ')
print(enterNum)

# Adding Two Numbers

num1 = int(input('enter num1: '))
num2 = int(input('enter num2: '))
sum = num1 + num2
print(sum)

# Addition of Two Float Number

fNum1 = float(input('enter num1: '))
fNum2 = float(input('enter num2: '))
sum = fNum1 + fNum2
print(sum)

# Oprators In Python

# Arithmetic Operators

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 // num2)

# Comparison  Operators

print(num1 == num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 != num2)

# Logical Operators

print(num1 > num2 and num1 > num2)
print(num1 > num2 or num1 > num2)
print(not num1 > num2)

# Assigment Operators

# Assignment Operators
assig = 5  #print one by one single
assig += 5
assig -= 2
assig *= 5
assig /= 5
print(assig)

# conditional operator

a = 34
b = 10
if (a > b):
  print("y")
else:
  print("n")

# write a program for voting using multiple condition

age = int(input('enter age: '))
if (age < 18):
  print("not eligible for voting")

elif (age >= 18 and age < 25):
  print("eligible for voting but not eligible for driving")

elif (age >= 25):
  print("eligible for voting and driving")

else:
  print("invalid age")


# email checker - using nested if
email = input('enter email: ')

if(email == 'nastynas@gmail.com'):
  print('welcome')
  password = input('enter password: ')
  if(password == 'nastynas'):
    print('login succesfully')
  else:
    print('incorrect password')
else:
  print('incorrect email')

#Looping Statement

#while Loop
i = 0
while i < 10:
    print(i)
    i = i +1

# for loop

for i in range(1,10,2):
    print(i)

# Jumping Statement
#break
i= 0

while True:
    i += 1
    print(i)
    if i == 10:
        break

#continue

i = 1

while i < 10:
  i += 1
  if(i == 5):
    continue
  print(i)


