# a=3200
# t=[]
# for i in range(2002,a,7):
#     if i%5!=0:
#         t.append(str(i))
# print(",".join(t))
# # "or" 
num=[i for i in range(2002,3200,7) if i%5!=0]
print(num)