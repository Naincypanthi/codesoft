num1=int(input("enter you number"))
num2=int(input("enter you number"))
ope=input("enter you operator")
if(ope=="+"):
    print(num1+num2)
elif(ope=="-"):
    print(num1-num2)
elif(ope=="*"):
    print(num1*num2)
elif(ope=="/"):
    print(num1/num2)
elif(ope=="%"):
    print(num1%num2)
else:
    print("INVALID OPERATOR")
