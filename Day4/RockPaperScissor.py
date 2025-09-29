import random
userInput=int(input("What do you choose 0 for Rock, 1 for Paper and 2 for scissor:"))
ComputerInput=random.randint(0,2)
print(f"Computer chose {ComputerInput}")

if(userInput==0 and ComputerInput==2) or (userInput==1 and ComputerInput==0) or (userInput==2 and ComputerInput==1):
    print("You Win")
elif(userInput==ComputerInput):
    print("It's a Draw")
elif(userInput!=0 and userInput!=1 and userInput!=2):
         print("Invalid Input")
else:
    print("You Lose")
# print(f"User Input is {userInput} and Computer Input is {ComputerInput}")    

