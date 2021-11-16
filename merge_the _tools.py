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

