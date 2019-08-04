import math
d=[1,23,3]
list1=[]
def calc(d,c=50,h=30):
    out=((2*c*d)/h)
    return out
sq= calc(d[1])
sq1= calc(d[0])
print(sq,sq1)
u=math.sqrt(int(sq))
i=round(u,2)
y=math.sqrt(int(sq1))
k=round(y,2)
list1.append(float(i))
list1.append(float(k))
print(list1)