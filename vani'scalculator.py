user = input("please enter your name:")
print(f"Hello {user}  welcome to Smart Calculator by : Vani Narwani ")
choice=input("what do you want to do:")
number1 =(int(input("please enter the first digits  that you want to calculate:")))
number2 = (int(input("please enter the second digits  that you want to calculate:")))
a=("the value of ",number1 ,"+","the value of", number2,"is:" ,number1 + number2)
b=("the value of ",number1 ,"-","the value of", number2,"is:" ,number1 - number2)
c=("the value of ",number1 ,"*","the value of", number2,"is:" ,number1 * number2)
d=("the value of ",number1 ,"/","the value of", number2,"is:" ,number2 / number1)
if choice=="+":
    print(a)
elif choice=="-":
    print(b)
elif choice=="*":
    print(c)
elif choice=="/":
    print(d)
else:
    print("please choose numbers:")