import module

choice = int(input('enter choice: '))

a = int(input('enter first number: '))
b = int(input('enter second number: '))



if(choice == 1):
    module.addition(a,b)
elif(choice == 2):
    module.substraction(a,b)
elif(choice == 3):
    module.multiplication(a,b)
elif(choice == 4):
    module.division(a,b)
else:
    print('invalid choice')