### HACKERRANK


## SUBSET

### The task is to find if Set A is a subset of Set B. The way I did is to separate Set A into a list and check if each element of Set A is in Set B. I set the result as `False` at first and if an element corresponds then the result is set True.
```py
t = 0
n_a = 0
n_b = 0
set_a = ''
set_b = ''
list_a = []
list_b = []
t = int(input())
for i in range(t):
    result = False
    n_a = int(input())
    set_a = str(input())
    n_b = int(input())
    set_b = str(input())
    list_a = set_a.split(' ')
    list_b = set_b.split(' ')
    for i in range(len(list_a)):
        if list_a[i] in list_b:
            result = True
    print(result)
```

## The Minion Game

### The task is to make words from a given word taking from each starting from each character. Here Stuart gets the score for words starting with consonants and Kevin gets for the vowels. 
```py
def minion_game(string):
    vowels = 'AEIOU'
    Stuart_score, Kevin_score = 0, 0
    length = len(string)
    score = 0
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    if Stuart_score < Kevin_score:
        print('Kevin {}'.format(Kevin_score))

if __name__ == '__main__':
    s = input()
    minion_game(s)
```


## Merge The Tools

### The task is to divide the given string into parts equal to it's factor and display such that no characters duplicate.
```py
def merge_the_tools(string, k):
    s = string
    f = ''
    t = ''
    for i in range(0, len(string), k):
        t = s[0:k]
        res = [j for n, j in enumerate(t) if j not in t[:n]]
        print(''.join(res))
        s = s[k:]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
```


## Time Delta

### The task is to find absolute time difference between two time stamps in seconds.  
### Like this:
```
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```
The code:
```py
def time_delta(t1, t2):
    first = datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    second = datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    print(first - second)
    return str(abs(int((first-second).total_seconds())))

if __name__ == '__main__':
    # t1, t2 = input(), input()
    print(time_delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000'))
```

## Find the Angle

### ABC is a right angled triange with right angle at B. M is the midpoint of side AC and M is connected to B. I have to find the angle MBC. The logic is simple: `Triangle MBC is an isosceles triangle, hence if I could find angle MCB then the job is done.` Which is exactly what i did.
```py
import math

degree_sign = u'\N{DEGREE SIGN}'

side_ab, side_bc = int(input()), int(input())
print(str(round(math.degrees(math.atan(side_ab/side_bc)))) + degree_sign)
``` 

## Happiness

### In this problem there are two sets A and B. We provide an array and if the elements of the array is in Set A then the add happy index by 1 or subtract by 1 if the element is in Set B.

```py
n_and_m = input()
integers = input().split(' ')
set_a = set(input().split(' '))
set_b = set(input().split(' '))
happy_index = 0
n_string = ''

for i in integers:
    if i in set_a:
        happy_index += 1
    elif i in set_b:
        happy_index -= 1

print(happy_index)
```

> I kept getting timeout errors - meaning the code took more time to execute than asked for - so when i used `set()` it decreased the time taken.

### Main takeaway: `set()`