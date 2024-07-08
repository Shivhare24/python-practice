# Problem
# find the maxium elements in an given arraay that would sum upto a given target

# Constraints:
# maxium elements in array is 25.

# Input
# 1. first line specifices the number of elements in the array plus the target
# 2. Second line specific the target
# 3.Subsequent line containes the elements of array(integers)


# output:_
# integers specfying the maxium number of that elements that sum up to a given target.
# return 0 if there is no match.

# Example
# input
# 5
# 10
# 2
# 3
# 5
# 5

# output:
# 3

def find_maximum_elements(arr):
    array=arr[2:]
    target=arr[1]
    start =0
    end =len(array)-1
    array.sort()
    sums = 0
    for i in array:
        sums += i
    diff = sums - target
    while ( end >= start):
        if diff == 0:
            print(array[start:end+1])
            return end - start+1
        elif diff - array[end] >= 0 :
            diff -= array[end]
            end -=1
        elif  diff < array[end]:
            diff -= array[start]
            start +=1
    return 0
        


if __name__ == '__main__':
    # arr = [6, 15, 10, 5, 2, 7, 1, 9]
    arr = [6,10, 1, 1, 2, 4, 4]
    print(find_maximum_elements(arr))