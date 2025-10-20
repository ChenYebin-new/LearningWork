from math import sqrt
def check(number):
    for i in range(3,int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def creat_num(num):
    for i in range(num,100000000):
        if check(i):
            return i
    return None
num = int(input())
record = num
res = []
index_pos = 2
aim_num = 2
while num>1:
    while num % aim_num == 0:
        num //= aim_num
        res.append(aim_num)
    aim_num = creat_num(index_pos+1)
    index_pos = aim_num

count_num = len(res)
ans = ""
for i in res:
    ans += str(i)
    if count_num > 1:
        count_num -= 1
        ans += "*"

print(f"{record}={ans}")