def get_midpoint(sequence)-> int:
    return (len(sequence)//2)

def binary_search(sequence, item)-> int:
    if item not in sequence:
        return -1
    if len(sequence) < 2:
        return sequence[0]
    midpoint = get_midpoint(sequence)
    if sequence[midpoint] == item:
        return midpoint
    elif sequence[midpoint] > item:
        point = binary_search(sequence[:midpoint], item)
        return midpoint - point
    else:
        point = binary_search(sequence[midpoint:], item)
        return midpoint + point


sequence_a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
item_a = 10

if __name__ == '__main__':
    print(binary_search(sequence_a,item_a))