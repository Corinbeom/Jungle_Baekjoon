c = int(input())  

for i in range(c):
    lst = list(map(int, input().split())) 
    
    sumNum = sum(lst[1:])  
    aver = sumNum / (len(lst) - 1)  

    avuLst = [num for num in lst[1:] if num > aver]  

    percent = (len(avuLst) / (len(lst) - 1)) * 100  

    print(f"{percent:.3f}%")  
