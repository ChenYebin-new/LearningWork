Input=input()
InputList=[]
while Input!="":
    InputList.append(Input)
    Input=input()
num = 0
for i in InputList:
    sen = i.split(' ')
    num += len(sen)
print(num,InputList)