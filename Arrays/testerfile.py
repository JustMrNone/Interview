x = input()
y = x.split()
z = []

for i in range(len(y)):
    z.append(int(y[i]))
for j in range(len(z)):
    print(type(z[j]))
        
print(z)