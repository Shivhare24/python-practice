#find duplicates
def find_duplicates(arr):
    my_dict = {}
    for i in arr:
        if i in my_dict:
            my_dict[i] = my_dict.get(i) + 1
        else:
            my_dict[i] = 1
    
    return list(filter(lambda key: my_dict[key] == max(my_dict.values()), my_dict.keys()))

if __name__ == '__main__':
    arr = [33, 34, 33, 4, 5, 5]
    print(find_duplicates(arr))


#Example of a generator
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)
for number in counter:
    print(number)

#print a sequence of number without any loop
def printNos(N):
    if N <= 0:
        return
    printNos(N-1)
    print(N)

printNos(9)

#find fibbonaci of a number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 9
if n <= 0:
    print('Invalid')
else:
    for i in range(n):
        print(fibonacci(i))


#transform the elements of the list as multiple of every other element except current.
def multiple_of(arr):
    result = []
    for i in range(len(arr)):
        x=1
        for id, value in enumerate(arr):
            if i != id:
                x*=value
        result.append(x)        
    print(result)

if __name__ == '__main__':
    arr = [1,2,3,4]
    multiple_of(arr)


#find 2nd largest element from an array
def second_largest_element(arr):
    largest = 0
    second_largest = 0
    
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i < largest:
            second_largest = i
    
    print(second_largest)



if __name__ == '__main__':
    arr = [3,10,6,4,1]
    second_largest_element(arr)


#flattern a nested dict
d = {'a': 1, 
     'c': {'a': 2, 'b': {'x': 5, 'y' : 10}},
     'd': [1, 2, 3]}

output = {'a': 1, 'c_a': 2, 'c_b_x': 5, 'c_b_y': 10, 'd': [1, 2, 3]}

def flatten_dict(d, separator='_', prefix=''):
    res = {}
    for key, value in d.items():
        if isinstance(value, dict):
            res.update(flatten_dict(value, separator, prefix + key + separator))
        else:
            res[prefix + key] = value
    return res

if __name__ == '__main__':
    print(flatten_dict(d))