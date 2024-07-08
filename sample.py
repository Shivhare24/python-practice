# def generate_even_numbers(start, end):
#     numbers =[]
#     for i in range(start, end):
#         if i % 2 ==0:
#             numbers.append(i)
    
#     return numbers

# print(generate_even_numbers(0, 10000))


def generate_even_numbers(start, end):
    for i in range(start, end):
        if i%2 == 0:
            yield i

even_number_generators = generate_even_numbers(0, 10)
another_even_number_generator = generate_even_numbers(10,30)

def loop(generators):
        while True:
            if not generators:
                return
            for i , generator in enumerate(generators):
                try:
                    print(next(generator))
                except StopIteration:
                    del generators[i]

loop([even_number_generators, another_even_number_generator])
