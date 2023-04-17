
print("*******THIS IS A CALCULATOR********")

'''
1= ADD
2= SUBTRACT
3= MULTIPLY
4= DIVIDE
'''
'''print("select an operation to perform: ")
print("1= ADD")
print("2= SUBTRACT")
print("3= MULTIPLY")
print("4= DIVIDE")
print("5")
'''
#operation= input()
'''print('Lets help you calculate any Mathematical problem you have!\nBut before we commence, here are somethings you need to know')
print('\nThe operators in this calculator are represented by the following numbers')
print('To add(+) type 1\nTo subtract(-) type 2\nTo divide(/) type 3\nTo multipy(x) type 4\nTo raise to the power(^) type 5\nTo squareroot a number type 6\nTo cuberoot a number type 7.\n\n\nSo now lets operate on some numbers!')
operator=float(input('Operator= '))
#if operator!=int():'''
 #   print('Numbers only')
operator=int(input('Operator= '))

if 1<=operator<=5:
    a=float(input('Enter your first number: '))
    b=float(input('Enter your second number: '))
    #numbers=int(str(input("enter digits and operators eg 1 a() 2 b() 3 e() 2:\n")))
    if operator==1:
        def sum():
            """Used to add two numbers"""
            summation=a+b
            return summation #Whenever i call my function, the result to this variable will show
        print(f'The summation of {a} and {b} is {sum()}')
    if operator==2:
        def sub():
            """Used to subtract two numbers"""
            subtraction=a-b
            return subtraction
        print(f'The subtraction of {a} and {b} is {sub()}')
    if operator==3:
        def div():
            """Used to divide two numbers"""
            divide=a/b
            return divide
        print(f'The division of {a} and {b} is {div()}')
    if operator==4:
        def mult():
            """Used to multiply two numbers"""
            multi=a*b
            return multi
        print(f'The multiplication of {a} and {b} is {mult()}')
    if operator==5:
        def power():
            """Used to raise to the power of numbers"""
            rpower=a**b
            return rpower
        print(f'The value of {a} raised to the power of {b} is {power()}')
#elif operator:
    #print('Pls use the numbers given. ')#Continue from here

#else:
    #print('Operator not in range. Use the numbers in the range given. ')

if operator==6 or operator==7:
    c=int(input('Enter a number: '))
    if operator==6:
        def sqrt():
            """Used to find the squareroot of a number"""
            sqroot=c*2*-1
            return sqroot
        print(f'The squareroot of {c} is {sqrt()}')
    elif operator==7:
        def cbrt():
            """Used to find the cuberoot of a number"""
            cbroot=c*3*-1 
            return cbroot
        print(f'The cuberoot of {c} is {cbrt()}')
    if operator==8:
        def equ():
           equation=int(str(input("enter digits and operators eg 1 a() 2 b() 3 e() 2:\n")))
           return equation
        
equ()
#power()