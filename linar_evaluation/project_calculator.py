print("*******THIS IS A CALCULATOR********")
print("So we're going to help you with your simple calculations.\n According to the instruction below select all that apply.")
'''
1= ADD
2= SUBTRACT
3= MULTIPLY
4= DIVIDE
'''
print("select an operation to perform: ")
print("1= PLUS")
print("2= MINUS")
print("3= DIVIDE")
print("4= TIMES")
print("5= POWER")
print("6= SQUAREROOT")
print("7= CUBEROOT")
def plus():
    """Used to add two numbers"""
    sum=a+b
    return sum #Whenever i call my function, the result to this variable will show    
operator=int(input('Operator= '))

if 1<=operator<=5:
    a=int(input('Enter your first digit: '))
    b=int(input('Enter your second digit: '))
    #numbers=int(str(input("enter digits and operators eg 1 a() 2 b() 3 e() 2:\n")))
    if operator==1:
        def plus():
            """Used to add two numbers"""
            sum=a+b
            return sum #Whenever i call my function, the result to this variable will show
        print(f'The sum of {a} and {b} is {plus()}')
    if operator==2:
        def minus():
            """Used to subtract two numbers"""
            subtract=a-b
            return subtract
        print(f'The subtraction of {a} and {b} is {minus()}')
    if operator==3:
        def div():
            """Used to divide two numbers"""
            divide=a/b
            return divide
        print(f'The division of {a} and {b} is {div()}')
    if operator==4:
        def multi():
            """Used to multiply two numbers"""
            multiply=a*b
            return multiply
        print(f'The multiplication of {a} and {b} is {multi()}')
    if operator==5:
        def power():
            """Used to raise to the power of numbers"""
            r_power=a**b
            return r_power
        print(f'The value of {a} raised to the power of {b} is {power()}')
elif operator:
    print('Pls use the numbers given. ')

else:
    print('Operator is not in range. Use the numbers provided in the range. ')

if operator==6 or operator==7:
    c=int(input('Enter a digit: '))
    if operator==6:
        def sqert():
            """Used to find the squareroot of a number"""
            sqeroot=c**2**-1
            return sqeroot
        print(f'The squareroot of {c} is {sqert()}')
    elif operator==7:
        def cbrt():
            """Used to find the cuberoot of a number"""
            cberoot=c**3**-1 
            return cberoot
        print(f'The cuberoot of {c} is {cbrt()}')

