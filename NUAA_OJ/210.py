slie = input()
n, k = slie.split()
n = int(n)
k = int(k)
A = []
B = []
for i in range(1, n + 1):
    if i % k == 0:
        A.append(i)
    else:
        B.append(i)
print("%.1f"%(sum(A)/len(A)),"%.1f"%(sum(B)/len(B)))