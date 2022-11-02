
# s1="Python"
# s2="python"

# if s1==s2:
#     print("Equal strings")
# else:
#     print("Not equal")


# if s1!=s2:
#     print("Not equal")
# else:
#     print("Equal strings")
    
    
#Guessing number Game

import random

#from random import randint



number=random.randint(1,5)


choice='y'

# while choice=='y':
#     x=input("Guess number:")
#     if str(number)==x:
#         print("Congradulations..your guess is correct!!")
#         break
        
#     else:
#         print("Sorry better luck next time")
#     choice=input("Do yu want to try again?[y/n]")
        
guess=True   
while guess==True:
    x=input("Guess number:")
    if str(number)==x:
        print("Congradulations..your guess is correct!!")
        guess=False
    else:
        print("Sorry better luck next time")
    














    
    