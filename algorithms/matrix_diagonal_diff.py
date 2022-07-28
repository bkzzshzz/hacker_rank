# arr = [[-1, 1, -7, -8], [-10, -8, -5, -2], [6, 9, 7, -1], [4, 4, -2, 1]]
arr = [[11,2,4], [4,5,6], [10, 8, -12]]
lead = 0
back = 0
n = len(arr)

for i in range(n):
    lead += arr[i][i]

for i in range(len(arr)):
    back += arr[i][n - 1]
    n -= 1

print(abs(lead-back))
#

# def diagonalDifference(arr):
#     # Write your code here
#     # lead = 0
#     # back = 0
#     # n = len(arr)
    
#     # for i in range(n):
#     #     lead += arr[i][i]
        
#     # for i in range(len(arr)):
#     #     back += arr[i][n - 1]
#     #     n -= 1
    
#     #     return abs(lead - back)
#     print(arr)
        
            

# if __name__ == '__main__':

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

