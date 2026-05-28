# first n=factorial method
# n=150
# result=[]
# for i in range(1,n+1):
#     if n%i==0:
#         result.append(i)
# print(result)

#second method
n=150
result=[]
for i in range(1,(n//2)+1):
    if n%i==0:
        result.append(i)

# result.append(n//2)git 
result.append(n)
print(result)

# third method 
# from math import sqrt
# n=150
# result=[]
# for i in range (1,int(sqrt(n)+1)):
#     if n%i==0:
#         result.append(i)
#         if n//i != i:
#             result.append(n//i)
# print(result)


    