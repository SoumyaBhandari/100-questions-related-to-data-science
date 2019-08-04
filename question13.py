test=input("enter")
letters=digits=0
for i in test:
    if i.isalpha():
        letters+=1
    elif i.isnumeric():
        digits+=1
    else:
        pass
print("the letters and didits",letters,digits)
