c = int(input("Please enter your int: "))
r = 2 * c + 1
x = r // 2 + 1
lst = [ [0 for i in range(r) ] for i in range(c)]

#[Debug]print(c, r, x)


for i in range(c):
    x -= 1
    for j in range(i+1):
        num = x + (2*j)
        if i == 0:
            lst[i][num] = 1
        elif i != 0:
            lst[i][num] = i+1

for i in range(c):
    for j in range(r):
        if lst[i][j] == 0:
            lst[i][j] = " "

for i in range(c):
    for j in range(r):
        print(lst[i][j], end = "")
    print()
