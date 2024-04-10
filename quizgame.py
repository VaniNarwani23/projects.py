import random

user=input("enter your name:")

print(f"hello {user} welcome to IQ quiz game:)")

questionsl=[" Which animal don't have legs?","What is the name given to a group of HORSES?",". What is the name given to a group of PEACOCKS?","Which one of these is not a musical instrument(use capital letters in ans)?"]
answers=["snake","harras","ostentation","MATBAN"]
u=random.choice(questionsl)
sum = 0
for i in range(len(questionsl)):
  print('Question number', i + 1)
  print(questionsl[i])
  ans = input('Please, enter the answer : ').lower()
  if (ans == answers[i]):
    print('Your answer is correct....')
    sum += 1000
    print('You won', sum, 'points. Congrats!')
    print()
  else:
    print("You're wrong... Try next time!")
    print()
    break

print('You won Rs.',
      sum,
      '/- in total. Congratulations!\nThankyou so much for playinig!...',
      sep='')


