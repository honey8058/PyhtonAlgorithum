# class solution:

def maxsubarray (arr,high):
    high = len(arr)
    total_sum = max_sum = nums[0]
    for i in nums[1:]:
        total_sum= max(i,total_sum+i)
        max_sum= max(max_sum,total_sum)

    return max_sum

    print(max_sum)
arr= [1,2,3,4]