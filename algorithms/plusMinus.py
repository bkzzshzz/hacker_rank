arr = [1, 1, 0, -1, -1]

# positiveCount = 0
# negativeCount = 0
# zeroCount = 0

# for i in range(len(arr)):
#     if arr[i] < 0:
#         negativeCount += 1
#     elif arr[i] > 0:
#         positiveCount += 1
#     elif arr[i] == 0:
#         zeroCount += 1
# positiveRatio = positiveCount/len(arr)
# print(format(positiveRatio, '.6f'))

def plusMinus(arr):
    # Write your code here
    positiveCount = 0
    negativeCount = 0
    zeroCount = 0
    
    for i in range(len(arr)):
        if arr[i] < 0:
            negativeCount += 1
        elif arr[i] > 0:
            positiveCount += 1
        elif arr[i] == 0:
            zeroCount += 1
    
    negativeRatio, positiveRatio, zeroRatio = negativeCount/len(arr), positiveCount/len(arr), zeroCount/len(arr)
    
    return format(positiveRatio, '.6f') + "\n" +format(negativeRatio, '.6f') + "\n" + format(zeroRatio, '.6f')

if __name__ == '__main__':
    print(plusMinus(arr))