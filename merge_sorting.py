# sabsa pehla do array ko sorted way mein merge karna hai 
def merge_array(left,right):
    i=0
    j=0
    n=len(left)
    m=len(right)
    result=[]
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1 
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_array=arr[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_array)
    return merge_array(left,right)

array=[1,5,8,2,9,4]
print(merge_sort(array))

