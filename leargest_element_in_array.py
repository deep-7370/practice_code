# first method
# nums=[55,32,-97,99,4,6]
# print(max(nums))

# second method
nums=[55,32,-97,99,4,6,900]
n=len(nums)
largest=nums[0]
for i in range(0,n):
    if nums[i]>largest:
        largest=nums[i]
print(largest)

