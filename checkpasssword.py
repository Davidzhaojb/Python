# 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。#设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
# 次数
count = 3
# 密码
password = "fishc"
while count:
    Password = input("请输入密码:")
    if Password == password:
        print("密码输入正确")
        break
    elif '*' in Password:
        print("密码中不能包含'*'，请重新输入，您还有",count,"次机会")
        continue
    else:
        print("密码输入错误,剩余",count-1,"次")
        count -= 1
print("游戏结束")
