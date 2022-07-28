num_list = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

def sum_big_numbers(ar):
    sum = 0
    sum = float(sum)

    for i in range(len(num_list)):
        sum = sum + num_list[i]

    return round(sum)

if __name__ == '__main__':
    print(sum_big_numbers(num_list))


