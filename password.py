import random
length=int(input("enter your password length"))
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
number="0123456789"
symbol=".,;:><?/\|+_)(-=@#^&*"
all=upper+lower+number+symbol
password="".join(random.sample(all,length))
print(password)