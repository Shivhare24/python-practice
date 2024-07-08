#Example 1:
#Input:
# [100, 200, 1, 3, 2, 4]
#
#Output:
# 4
#
#Explanation:
# The longest consecutive subsequence is 1, 2, 3, and 4.
#
#Input:
# [3, 8, 5, 7, 6]
#
#Output:
# 4
#
#Explanation:
# The longest consecutive subsequence is 5, 6, 7, and 8.

def longest_consecutive_sequence(arr):
    subsequence = []
    for i in arr:
            if not i in subsequence and ((i+1) in arr or (i-1) in arr):
                subsequence.append(i)
    subsequence.sort()
    
    return subsequence

def check(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i]  != 1:
            count+=1
            print(count)

    if count > 1:
        return False
    else:
        return True

if __name__ == '__main__':
    arr = [3, 8, 5, 7, 6, 10, 11, 12]
    print(longest_consecutive_sequence(arr))
    # nums = [3, 8, 5, 7, 6]
    # print(check(nums))
