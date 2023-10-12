# Question : Take Subject Marks And Calculate Average

sub1 = float(input('enter sub1 marks: '))
sub2 = float(input('enter sub2 marks: '))
sub3 = float(input('enter sub3 marks: '))
sub4 = float(input('enter sub4 marks: '))
sub5 = float(input('enter sub5 marks: '))
avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
print(avg)

# Question : Swapping of two numbers

num1 = int(input('enter num1: '))
num2 = int(input('enter num2: '))
num3 = num1
num1 = num2
num2 = num3
print(num1, num2)

# check weather the number is positive,negative or zero 

num = int(input('enter num: '))
if (num > 0):
  print("positive")
elif (num < 0):
  print("negative")
else:
  print("zero")