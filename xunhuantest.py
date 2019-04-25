# 循环练习题
# 按照100分制，90分以上为A，80-90为B，60-80为C，60一下为D
# 写一个程序，当用户输入分数，自动转换为ABCD的形式打印

#方法一
score = int("请输入一个分数：")
if 100>= score >= 90:
    print("A")
if 90>= score >= 80:
    print("B")
if 80>= score >= 60:
    print("C")
if 60>= score >= 0:
    print("D")
if 100 < score or score < 0:
    print("输入错误!")

#方法二
if 100 >= score >= 90:
    print("A")
elif 90>= score >= 80:
    print("B")
elif 80>= score >= 60:
    print("C")
elif 60>= score >= 0:
    print("D")
else:
    print("输入错误！")
