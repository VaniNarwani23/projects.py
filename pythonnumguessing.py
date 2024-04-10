print("Number Guesssing game: by Vani Narwani")
import random

user=(int(input("enter your number:"))) 
comp=random.randint(0,10)
def check(user,comp):
 
  if (user==comp):
    print("you both selected same numbers:",{comp},{user})
    return 1
  elif(user!=comp):
       print("you both selected different number:")
       return 0
  else:
    print("you both selected different number:")



score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("you lose")
elif (score == 1):
  print("You won")
else:
  print("You lose")
  



