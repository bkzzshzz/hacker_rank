
w = '5 5'
x = '999999991 999999992 999999993 999999994 999999999'
y = '999999991 999999993 999999995 999999999 999999997'
z = '999999990 999999992 999999996 999999998 999999994'

import time
start = time.perf_counter()
n_and_m = w
integers = x.split(' ')
set_a = set(y.split(' '))
set_b = set(z.split(' '))
happy_index = 0
n_string = ''

for i in integers:
    if i in set_a:
        happy_index += 1
    elif i in set_b:
        happy_index -= 1

print(happy_index)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
n_and_m = w
integers = x.split(' ')
set_a = y.split(' ')
set_b = z.split(' ')
happy_index = 0
n_string = ''

for i in integers:
    if i in set_a:
        happy_index += 1
    elif i in set_b:
        happy_index -= 1

print(happy_index)
end = time.perf_counter()
print(end - start)