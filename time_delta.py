import datetime

# def time_delta(t1, t2):
#     days = {
#         'Sun' : 1,
#         'Mon' : 2,
#         'Tue' : 3,
#         'Wed' : 4,
#         'Thu' : 5,
#         'Fri' : 6,
#         'Sat' : 7
#     }

#     months = {
#         'Jan' : 1,
#         'Feb' : 2,
#         'Mar' : 3,
#         'Apr' : 4,
#         'May' : 5,
#         'Jun' : 6,
#         'Jul' : 7,
#         'Aug' : 8,
#         'Sep' : 9,
#         'Oct' : 10,
#         'Nov' : 11,
#         'Dec' : 12
#     }

#     t1 = t1.split(' ')
#     day1, date1, month1, year1, time1, timezone1 = t1[0], t1[1], t1[2], t1[3], t1[4], t1[5][-4:]
#     time1 = time1.split(':')
#     hr1, min1, sec1 =  time1[0], time1[1], time1[2]
#     timezone1hr, timezone1min = timezone1[:2], timezone1[2:]
    
#     t2 = t2.split(' ')
#     day2, date2, month2, year2, time2, timezone2 = t2[0], t2[1], t2[2], t2[3], t2[4], t2[5][-4:]
#     time2 = time2.split(':')
#     hr2, min2, sec2 =  time2[0], time2[1], time2[2]
#     timezone2hr, timezone2min = timezone2[:2], timezone2[2:]
#     # print(min1, min2)

#     # print(abs(int(date1) - int(date2)) * 86400, abs(int(hr1) - int(hr2)) * 3600, abs(int(min1) - int(min2)) * 60, abs(int(sec1) - int(sec2)), abs(int(timezone1hr) - int(timezone2hr)) * 3600, abs(int(timezone1min) - int(timezone2min)) * 60)

#     first = abs(int(date1)) * 86400 + abs(int(hr1)) * 3600 + abs(int(min1)) * 60 + abs(int(sec1)) + abs(int(timezone1hr)) * 3600 + abs(int(timezone1min)) * 60
#     second = abs(int(date2)) * 86400 + abs(int(hr2)) * 3600 + abs(int(min2)) * 60 + abs(int(sec2)) + abs(int(timezone2hr)) * 3600 + abs(int(timezone2min)) * 60
#     print(first -  second)
#     print(abs(int(date1) - int(date2)) * 86400 + abs(int(hr1) - int(hr2)) * 3600 + abs(int(min1) - int(min2)) * 60 + abs(int(sec1) - int(sec2)) + abs(int(timezone1hr) - int(timezone2hr)) * 3600 + abs(int(timezone1min) - int(timezone2min)) * 60)

    

# if __name__ == '__main__':
#     t1, t2 = 'Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000'
#     time_delta(t1, t2)


def time_delta(t1, t2):
    first = datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    second = datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    print(first - second)
    return str(abs(int((first-second).total_seconds())))

if __name__ == '__main__':
    # t1, t2 = input(), input()
    print(time_delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000'))
