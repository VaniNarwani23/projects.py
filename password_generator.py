import random
CHARACTER_SET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
NUMBERS_SET=['0','1','2','3','4','5','6','7','8','9']
SYMBOLS_SET=['!','@','#','$','%','^','&','*','+','-','<','>','(',')',':','?']
n_CHARACTER_SET=int(input("how many characters you want in your password?\n"))
n_NUMBERS_SET=int(input("how many NUMBERS you want in your password?\n"))
n_SYMBOLS=int(input("how many Symbols you want in your password?\n"))
password=''
for i in range(1,n_CHARACTER_SET+1):
    char=random.choice(CHARACTER_SET)
    password += char
for i in range(1,n_NUMBERS_SET+1):
    char=random.choice(NUMBERS_SET)
    password += char
for i in range(1,n_SYMBOLS+1):
    char=random.choice(SYMBOLS_SET)
    password += char
print(f"your password is generated:{password}")