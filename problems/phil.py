
x = int(input())

y = list(str(x))
z = []
for i in y:
    z.append(i)
k = z[::-1]

if z == k:
    print(True)
else:
    print(False)