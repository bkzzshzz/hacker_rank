# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'compareTriplets' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY a
# #  2. INTEGER_ARRAY b
# #

# def compareTriplets(a, b):
#     # Write your code here
#     alice_point, bob_point = 0, 0
#     for i in range(3):
#         print(i, a[i], b[i])
#         if a[i] > b[i]:
#             alice_point += 1
#         elif b[i] > a[i]:
#             bob_point += 1
#     return list(alice_point).append(list(bob_point))

# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     # print(result)

#     # fptr.write(' '.join(map(str, result)))
#     # fptr.write('\n')

#     # fptr.close()


a = [1, 2, 3]
b = [4, 2, 6]
a_c = 0
b_c = 0
for i in range(3):
    if a[i] > b[i]:
        a_c += 1
    elif b[i] > a[i]:
        b_c += 1
d = [a_c, b_c]
print(d)

