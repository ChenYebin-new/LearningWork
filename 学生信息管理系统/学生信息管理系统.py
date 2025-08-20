"""
学生信息管理系统, 自己跟着案例录播实现一遍  把每一个直接点回顾一下增加记忆力
"""
"""请在下方实现"""
# 这个作业不要求提交 自己跟着录播敲一遍  其他2个作业需要提交     

import os
import json

str_info = """**************************************************
欢迎使用【学生信息管理系统】V1.0
请选择你想要进行的操作
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 修改学生信息
5. 删除学生信息

0. 退出系统
**************************************************"""

def update_data(students_list):
    with open("students_list.json", "w", encoding="utf-8") as f:
        sec = json.dumps(students_list, ensure_ascii=False)
        f.write(sec)
def ask_for_data():
    """询问是否保留原有数据"""
    act = input("请问是否保留原有数据?\n如无需保留请输入1,否则请直接回车即可\n:")
    if act == '1':
        if os.path.exists("students_list.json"):
            os.remove("students_list.json")
def check_data():

    students_list = []
    if os.path.exists("students_list.json"):
        print("原有数据加载成功\n")
        with open("students_list.json", "r", encoding="utf-8") as f:
            students_list = json.load(f)
    else:
        with open("students_list.json", "w", encoding="utf-8") as f:
            sec = json.dumps(students_list, ensure_ascii=False)
            f.write(sec)
        print("数据库已完成初始化\n")
    return students_list
def creat_account(students_list):
    """获取输入的数据"""
    while True:
        name = input("请输入学生姓名:")
        try:
            chinese = int(input("请输入语文成绩:"))
            english = int(input("请输入英语成绩:"))
            math = int(input("请输入数学成绩:"))
            total = chinese + english + math
        except ValueError:
            print("请尝试重新输入,注意不要输入非数字")
            continue
        """将新的数据存储"""

        dic = {"name": name, "chinese": chinese,
               "english": english, "math": math,
               "total": total, }
        students_list.append(dic)
        with open("students_list.json", "w", encoding="utf-8") as f:
            json.dump(students_list, f, ensure_ascii=False)
        return dic["name"]
def show_info(students_list):
    """显示所有学生信息"""
    if students_list == []:
        print("数据库中暂无学生信息")

    else:
        print("姓名\t\t语文\t\t英语\t\t数学\t\t总分")
        print("-"*50)
        str_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"
        for dic in students_list:

            print(str_format.format(*dic.values()))
            # print(dic["name"],dic["chinese"],dic["english"],dic["math"],dic["total"],sep="\t\t")
            print("-"*50)
def search_info(students_list):
    FLAG = '1'
    while FLAG == "1":
        name = input("请输入您要查询学生的姓名:")
        flag1 = False
        for dic in students_list:
            if dic["name"] == name:
                print("姓名\t\t语文\t\t英语\t\t数学\t\t总分")
                str_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"
                print(str_format.format(*dic.values()))
                flag1 = True
                break
        if not flag1:
            print("抱歉,数据库中没有学生相关信息")
            FLAG = input("您所查询数据如上,是否需要继续查询?\n如不需要请输入0,否则输入1:")
        else:
            print("-"*50)
            FLAG = input("您所查询数据如上,是否需要继续查询?\n如不需要请输入0,否则输入1:")
def change_info(students_list):
    FLAG = '1'
    while FLAG == "1":
        name = input("请输入要修改的学生姓名:")
        flag1 = False
        flag2 = False
        for dic in students_list:
            if dic["name"] == name:
                print("已找到目标学生数据,可以进行修改.......")
                try:
                    chinese = int(input("请输入语文成绩:"))
                    english = int(input("请输入英语成绩:"))
                    math = int(input("请输入数学成绩:"))
                    total = chinese + english + math
                except ValueError:
                    print("请尝试重新输入,注意不要输入非数字")
                    flag2 = True
                    break
                dic1 = {"name": name, "chinese": chinese,
                       "english": english, "math": math,
                       "total": total, }
                students_list.remove(dic)
                students_list.append(dic1)
                update_data(students_list)
                flag1 = True
                break
        if flag2:
            continue
        if not flag1:
            print("抱歉数据库中没有目标学生相关信息")
            FLAG = input("是否需要继续修改?\n如不需要请输入0否则输入1:")
        else:
            print("-"*50)
            FLAG = input("您已经成功完成修改,是否需要继续修改?\n如不需要请输入0否则输入1:")
def delete_info(students_list):
    while True:
        name = input("请输入要删除的学生姓名:")
        flag1 = False
        for dic in students_list:
            if dic["name"] == name:
                print("已经成功锁定目标学生信息,正在进行删除.......")
                students_list.remove(dic)
                update_data(students_list)
                flag1 = True
                break
        if not flag1:
            print("数据库中未能检索到相关学生信息")
            FLAG = input("是否需要继续删除?\n如不需要请输入0否则输入1:")
        else:
            print("-"*50)
            print("已经成功完成删除")
            FLAG = input("是否需要继续删除?\n如不需要请输入0否则输入1:")

if __name__ == '__main__':
    ask_for_data()

    flag = False
    while True:

        if not flag:
            students_list = check_data()
            flag = True

        print(str_info)
        action = input("请输入数字代表您的操作:")

        if action == '1':

            print("即将新建学生信息")
            name = creat_account(students_list)
            print(f"-------成功添加{name}的信息---------------")

        elif action == '2':

            print("即将显示全部信息")
            show_info(students_list)
            print("学生信息显示完毕")

        elif action == '3':
            print("即将查询学生信息")
            search_info(students_list)
            print("查询完毕")

        elif action == '4':
            print("即将修改学生信息")
            change_info(students_list)
            print("修改完毕")
        elif action == '5':
            print("即将删除学生信息")
            delete_info(students_list)
            print("删除完毕")

        elif action == '0':
            print("即将退出系统")
            print("--------------------------------------")
            print("您已退出系统，再见！！")
            break
        else:
            print("请输入正确的序号")
