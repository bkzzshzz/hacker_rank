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
        
    