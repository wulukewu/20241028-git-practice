n = 10
m = 9
arr = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr[i][j] = i * j + 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end='\t')
    print()

print(arr)