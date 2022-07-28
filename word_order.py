from os import system
n = int(input())

distinct = 0
a = []
for i in range(n):
    a.append(input())
for i in range(len(a)):
    if a[i] not in a[i+1:]:
        distinct += 1
_ = system('clear')
for i in a:
    count = a.count(i)
    while i in a:
        a.remove(i)
    print(a)
    print(count)


        



print(distinct)
'''
bcdef
abcdefg
bcde
bcdef
'''