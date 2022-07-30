def birthdayCakeCandle(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    candles = [2, 5, 6, 7, 8, 9, 9]
    print(birthdayCakeCandle(candles))


