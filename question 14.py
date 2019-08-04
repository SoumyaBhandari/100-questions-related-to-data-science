test=input("enter")
Up=0
Low=0
for i in test:
    if i.isupper():
        Up+=1
    elif i.islower():
        Low+=1
    else:
        pass
print("upper case:",Up)
print("lower case",Low)
