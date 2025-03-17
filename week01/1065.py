def han(n):
    count = 0
    for i in range(1,n+1):
        a = str(i)
        if len(a) <= 2:
            count = count + 1
        elif len(a)== 3:
            if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]):
                count = count + 1
        elif len(a) == 4:
            if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]) == int(a[2]) - int(a[3]):
                count = count + 1
                
    print(count)

n = int(input())

han(n)