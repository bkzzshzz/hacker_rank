def gradeCheck(n):
    j = []
    for i in n:
        if int(i) < 38:
            j.append(i)
        else:
            m = int(i)
            
            while m % 5 != 0:
                m += 1

            if m - int(i) < 3:
                j.append(m)
            else:
                j.append(i)
    return j

if __name__ == '__main__':
    grades = [73, 67, 38, 33]
    print(gradeCheck(grades))
 
