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