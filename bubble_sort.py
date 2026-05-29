nums=[1,4,7,2,5,8,3,6]
def bubble_sort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap=True
    if is_swap==False:

        return nums
print(bubble_sort(nums))