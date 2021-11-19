# #Manual String Formatting using f-string

# def manual_str_formatting(name, subscribers):
#     if subscribers > 100000:
#         print("Wow " + name + "! You have " + str(subscribers) + " subscribers")
#     else:
#         print("Lol " + name + " that's not many subs")

# manual_str_formatting('Bikesh', 150000)

# def manual_str_formatting(name, subscribers):
#     if subscribers > 100000:
#         print(f"Wow {name}! You have {subscribers} subscribers")
#     else:
#         print(f"Lol {name} that's not many subs")

# manual_str_formatting('Bikesh', 150000)

# # Closing a file

# def manually_calling_close_on_a_file(filename):
#     f = open(filename, "w")
#     f.write("Hello!\n")
#     f.close()

# def manually_calling_close_on_a_file(filename):
#     with open(filename) as f:
#         f.write("Hello\n")

# # ^ is not for exponentiation

# def caret_and_exponentiation(x, p):
#     y = x ^ p # bitwise xor
#     y = x ** p

# LATER
# def always_using_comprehensions(a, b, n):
#     """matrix product of a, b of length n x n"""
#     c = []
#     for i in range(n):
#         for j in range(n):
#             ij_entry = sum(a[n * i + k] * b[n * k + j] for k in range(n))
#             c.append(ij_entry)
#     return c

# a = [[1,2], [2,4]]
# b = [[3,4], [5,6]]
# n = 2
# always_using_comprehensions(a, b, n)

## using is instead of == to check for none/singletons like None, True, False

# def equality_for_singletons(x):
#     if x == None:
#         pass
#     if x == True:
#         pass
#     if x == False:
#         pass

# def equality_for_singletons(x):
#     if x is None:
#         pass
#     if x is True:
#         pass
#     if x is False:
#         pass

#interesting
# message = 'hi'
# fill = 's'
# align = '>'
# width = 10
# print(f'{message:{fill}>{width}}')

# Range Len Pattern

# def range_len_pattern():
#     a = [1, 2, 3]
#     for i in range(len(a)):
#         v = a[i]
#         print(v)

# def range_len_pattern():
#     a = [1, 2, 3]
#     for v in a:
#         print(v)

# # To get index and the element use enumerate

# def range_len_pattern():
#     a = [1, 2, 5]
#     for i, v in enumerate(a):
#         print(i, v)

# # use ZIP to interact with elements in two lists

# def range_len_pattern():
#     a = [1, 2, 4]
#     b = [4, 5, 6]
#     c = [7, 8, 9]
#     for av, bv, cv in zip(a, b, c):
#         print(av, bv, cv)

# if there's still need for index then use enumerate

# def range_len_pattern():
#     a = [1, 2, 3]
#     b = [4, 5, 6]
#     for av, bv in enumerate(zip(a, b)):
#         print(av, bv)

# range_len_pattern()

# 13. Looping over the keys to a dictionary

# def for_key_in_dict_keys():
#     d = {
#         'a' : 1,
#         'b' : 2,
#         'c' : 3,
#     }
#     for key in d:
#         print(key)

# for_key_in_dict_keys()

# def for_key_in_dict_keys():
#     d = {
#         'a' : 1,
#         'b' : 2,
#         'c' : 3,
#     }
#     print(list(d)) #makes list of keys only
#     for key in list(d):
#         print(key)

# for_key_in_dict_keys()

# def not_using_dict_items():
#     d = {
#         'a' : 1,
#         'b' : 2,
#         'c' : 3,
#     }
#     for key, val in d.items():
#         print(key, val)
# not_using_dict_items()

# not using tuple unpacking

# def not_using_tuple_unpacking():
#     mytuple = 1, 2
#     x = mytuple[0]
#     y = mytuple[1]
#     print(x, y)
# not_using_tuple_unpacking()

# def not_using_tuple_unpacking():
#     mytuple = 1, 2
#     x, y = mytuple
#     print(x, y)
# not_using_tuple_unpacking()

# To calculate the time it took to run the code

# import time

# this calculates accurate time
# def timing_with_time():
#     start = time.perf_counter()
#     time.sleep(1)
#     end = time.perf_counter()
#     print(end - start)
# timing_with_time()


# time.time means the current time on the clock
# import time

# def timing_with_time():
#     start = time.time()
#     time.sleep(1)
#     end = time.time()
#     print(end - start)
# timing_with_time()

