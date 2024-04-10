import time

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d  %H:%M:%S", t)

print(formatted_time)

to_do_list = []

# Add items to the to do list
user=to_do_list.append(input("enter the work:"))
u=(input("do you want to add more ?:"))
if u=='yes':
   r=input("write here:")
   to_do_list.append(r)
    
print(to_do_list)

done=input("do you want to remove anything? ")
if done=='yes':
   rve=(input("what you want to remove? "))
   to_do_list.remove(rve)
print(to_do_list)