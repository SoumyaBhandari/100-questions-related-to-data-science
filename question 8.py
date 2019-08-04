u=[]
u.extend(input("enter charcters").split(","))
k=sorted(u)
l=",".join(k)
print(l)
print(l.replace(" ",","))