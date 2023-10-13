# functions in Py

def demo():
  print('hello world')

demo()

#Odd Even
def odd_even(num):
  if num % 2 == 0:
    print("Even")
  else:
    print("Odd")

odd_even(int(input("Enter a number: ")))

# addition function

def addition(a,b =5):
  c =  a+b
  print(c)

x = int(input('enter num x: '))
y = int(input('enter num y: '))
addition(x,y)
