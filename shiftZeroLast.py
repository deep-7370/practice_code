# def shiftZeroLast(arr):
#     for i in arr:
#         if i==0:
#             arr.remove(i)
#             arr.append(i)
#     return arr
# ss=[11,0,5,0,2,3,8,0,1,0]
# print(shiftZeroLast(ss))


def shiftZeroLast(arr):
    arr1=[]
    arr2=[]
    for i in arr:
        if i>0:
            arr1.append(i)
        else:
            arr2.append(i)
    s=arr1+arr2
    arr[:]=s[:]
    return arr

ss=[11,0,5,0,2,3,8,0,1,0]
print(shiftZeroLast(ss))

