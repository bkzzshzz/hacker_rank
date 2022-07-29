def minMAxSum(arr):
    arr = sorted(arr)

    minSum = sum(arr[:4])
    maxSum = sum(arr[1:])

    print(minSum, maxSum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    minMAxSum(arr)
