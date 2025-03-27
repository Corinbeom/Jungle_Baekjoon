main_str = input()

boom_str = input()

boom_len =len(boom_str)

stack = []

for bw in main_str:
    stack.append(bw)
    if len(stack) >= boom_len:
        if ''.join(stack[-boom_len:]) == boom_str:
            for _ in range(boom_len):
                stack.pop()
                
result = ''.join(stack)
print(result if result else "FRULA")