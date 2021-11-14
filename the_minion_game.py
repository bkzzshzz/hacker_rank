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
    # My orginal code does not work for bulky words
    # string = string.upper()
    # words = []
    # kevin_count = 0
    # stuart_count = 0
    # for i in range(len(string)):
    #     string1 = string[i:]
    #     for i in range(len(string1)):
    #         words.append(string1[0:i+1])
    # try:
    #     print(len(words))
    # except err as e:
    #     print(e)
    # words.sort()
    # for i in range(len(words)):
    #     if str(words[i][0]) in "AEIOU":
    #         kevin_count += 1
    #     else:
    #         stuart_count += 1
    # if kevin_count > stuart_count:
    #     print(f'Kevin {kevin_count}')
    # elif stuart_count > kevin_count:
    #     print(f'Stuart {stuart_count}')
    # else:
    #     print('Draw')
        

if __name__ == '__main__':
    s = input()
    minion_game(s)