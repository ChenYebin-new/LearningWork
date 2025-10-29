num = input()
num = num.split()
a = int(num[0])
b = int(num[1])
tot = 0
for i in range(b):
    temp = 0
    for j in range(i+1):
        temp += a*(10**j)
    tot += temp
print(tot)