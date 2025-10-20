def check(temp):
    a1 = temp%10
    a2 = (temp//10)%10
    a3 = (temp//100)%10
    if a1**3+a2**3+a3**3==temp:
        return True
    else:
        return False

for i in range(100,1000):
    temp = i
    if check(temp):
        print(temp,end=' ')
