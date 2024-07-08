def find_duplicates(arr):
    my_set = set()
    out = []
    for i in arr:
        if i in my_set:
            out.append(i)
        else:
            my_set.add(i)
    
    return out

if __name__ == '__main__':
    arr = [33, 34, 33, 4, 5, 5]
    print(find_duplicates(arr))