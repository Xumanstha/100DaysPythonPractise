def calculate_love_score(name1, name2):
    combined_names=(name1 + name2).lower()
    t=combined_names.count('t')
    r=combined_names.count('r')
    u=combined_names.count('u')
    e=combined_names.count('e')
    digits1=t+r+u+e
    l=combined_names.count('l')
    o=combined_names.count('o')     
    v=combined_names.count('v')
    e=combined_names.count('e')
    digits2=l+o+v+e
    love_score=int(str(digits1)+str(digits2))
    return love_score

name1=input("Enter your name: ")
name2=input("Enter their name: ")
score=calculate_love_score(name1, name2)
print(f"Your love score is: {score}")
if (score<10) or (score>90):
    print("You go together like coke and mentos.")
elif (score>=40) and (score<=50):
    print("You are alright together.")
else:
    print("Your love score is just average.")   
   
