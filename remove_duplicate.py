# first method for remove duplicate
nums=[1,1,1,1,2,3,4,4,5,6,7,7,8] 
nums=list(set(nums))
nums.sort()
print(nums)
duplicate_element=[]
