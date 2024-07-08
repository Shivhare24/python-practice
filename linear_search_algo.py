def linear_search(sequence, item):
    if len(sequence) == 1:
        return 0
    for i in range(0, len(sequence)):
        if sequence[i]==item:
            return i
    return -1
sequence_a = [1,2,3,4,5,6,7,8,9]
item_a = 7

if __name__ == '__main__':
    print(linear_search(sequence_a,item_a))