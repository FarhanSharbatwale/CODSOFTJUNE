def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        print("Oops! Divide by zero Error. Enter valid input")
        return 'Error'
    else:
        return a/b

while True:
    print("------CALCULATOR------")
    print("Enter a choice\n1)Add\n2)Subtract\n3)Multiply\n4)Divide\n5)Exit")
    choice = int(input("Enter a choice : "))
    if choice == 5:
        print("Program Exited...")
        break
    else:
        n1 = int(input("Enter the first number : "))
        n2 = int(input("Enter the second number : "))
        if choice == 1:
            c = add(n1,n2)
            print("The sum is : ",c)
        elif choice == 2:
            c = subtract(n1,n2)
            print("The difference is : ",c)
        elif choice == 3:
            c = multiply(n1,n2)
            print("The multiplication is : ",c)
        elif choice == 4:
            c = divide(n1,n2)
            if c != 'Error':
                print("The division is : ",c)
        else:
            print("Enter a valid input")
    
        
    
 
    
