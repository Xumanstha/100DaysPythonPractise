def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    '+':add,
    '-':sub,
    '*':multiply,
    '/':divide
}


# print("+\n-\n*\n/\n")



def calculator():
    should_continue=True
    a=int(input("What's the first number: "))

    while should_continue:

        for operation in operations:
            print(operation)

        user_operation=input("Choose one operation: ")

        b=int(input("What's the next number: "))

        result=operations[user_operation](a,b)

        print(f"{a}{user_operation}{b}={result}")

        choice=input(f"press 'y' to continue working with {result} or press 'n' to start new calculation: ")

        if choice=='y':
            a=result
        elif choice=='n':
            should_continue=False
            print("\n"*20)
            calculator()
        else:
            should_continue=False

    
calculator()

