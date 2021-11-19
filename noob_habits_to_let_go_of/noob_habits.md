### Manual String Formatting

### Instead of using `+` sign to add string when printing like:

```py
def manual_str_formatting(name, subscribers):
    if subscribers > 100000:
        print("Wow " + name + "! You have " + str(subscribers) + " subscribers")
    else:
        print("Lol " + name + " that's not many subs")

manual_str_formatting('Bikesh', 150000)
```

### We can use the f-string formatting when we enclose variables in curly brackets and the plus point is that it is more readable.

```py
def manual_str_formatting(name, subscribers):
    if subscribers > 100000:
        print(f"Wow {name}! You have {subscribers} subscribers")
    else:
        print(f"Lol {name} that's not many subs")

manual_str_formatting('Bikesh', 150000)
```

### Open files with `with` statement rather than normal opening and closing

```py
def manually_calling_close_on_a_file(filename):
    f = open(filename, "w")
    f.write("Hello!\n")
    f.close()
```
### This is better.
```py
def manually_calling_close_on_a_file(filename):
    with open(filename) as f:
        f.write("Hello\n")
```

### The caret symbol `^` is not for `exponentiation` but it is for `bitwise xor`

```py
def caret_and_exponentiation(x, p):
    y = x ^ p # bitwise xor
    y = x ** p
```

### Use `is` instead of `==` when checking for singletons like `None, True, False`
```py
def equality_for_singletons(x):
    if x == None:
        pass
    if x == True:
        pass
    if x == False:
    pass
```
### Like:
```py
def equality_for_singletons(x):
    if x is None:
        pass
    if x is True:
        pass
    if x is False:
        pass
```

### Instead of using indices we can loop in values of a list
```py
def range_len_pattern():
    a = [1, 2, 3]
    for i in range(len(a)):
        v = a[i]
        print(v)
```
### This is better.
```py
def range_len_pattern():
    a = [1, 2, 3]
    for v in a:
        print(v)
```

### To access index and elements in a list use `enumerate()`

### Here `i` is the index of the corresponding element `v`
```py
def range_len_pattern():
    a = [1, 2, 5]
    for i, v in enumerate(a):
        print(i, v)
```

### To access elements from two or more lists use `zip()`

```py
def range_len_pattern():
    a = [1, 2, 4]
    b = [4, 5, 6]
    for av, bv, cv in zip(a, b):
        print(av, bv)

def range_len_pattern():
    a = [1, 2, 4]
    b = [4, 5, 6]
    c = [7, 8, 9]
    for av, bv, cv in zip(a, b, c):
        print(av, bv, cv)
```

### When you want the positions of elements of two lists use `zip()` within `enumerate()`

```py
def range_len_pattern():
    a = [1, 2, 3]
    b = [4, 5, 6]
    for av, bv in enumerate(zip(a, b)):
        print(av, bv)
```

### Keys in a dictionary

### Here this only loops over the keys
```py
def for_key_in_dict_keys():
    d = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
    }
    for key in d:
        print(key)
```
### This too loop over the keys
```py
def for_key_in_dict_keys():
    d = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
    }
    print(list(d)) #makes list of keys only
    for key in list(d):
        print(key)
```
### Use dict`.items()` to access the values too
```py
def not_using_dict_items():
    d = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
    }
    for key, val in d.items():
        print(key, val)
```

### Tuple unpacking

```py
def not_using_tuple_unpacking():
    mytuple = 1, 2
    x = mytuple[0]
    y = mytuple[1]
    print(x, y)
not_using_tuple_unpacking()
```
### This is better
```py
def not_using_tuple_unpacking():
    mytuple = 1, 2
    x, y = mytuple
    print(x, y)
not_using_tuple_unpacking()
```
### To calculate the time it took to run the code

### Use `time.perf_counter()` to calculate time taken to run operations
```py
import time

def timing_with_time():
    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter()
    print(end - start)
timing_with_time()
```
### `time.time` involves the system clock 
```py
import time

def timing_with_time():
    start = time.time()
    time.sleep(1)
    end = time.time()
    print(end - start)
timing_with_time()
```










