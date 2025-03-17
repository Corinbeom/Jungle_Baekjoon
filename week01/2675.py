tc = int(input())
triple = []

for i in range(tc):
    n, str = (input().split())
    for j in range(len(str)):
        triple += str[j] * int(n)
    
    print("".join(triple))
    n = ""
    triple = []
    j = 0
