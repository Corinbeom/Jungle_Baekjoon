expr = input().strip()
chunks = expr.split('-')
values = [sum(map(int, chunk.split('+'))) for chunk in chunks]
print(values[0] - sum(values[1:]))
