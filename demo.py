import random;
index = 1
numran = random.randint(1,10)
# print("numran的值是"+numran)
print("-----------------欢迎来到小黑鱼的工作室-------------------")
print("-_-下面开始答题了额")
num = input("请输入一个你喜欢的数字:")
temp = int(num)
while temp != numran and index <=3:
#print("兄弟，第"+index+"次机会，好好把握")
    if temp > numran:
        print("兄弟，猜大了，再来一次吧")
    if temp < numran:
        print("兄弟，小了呀,再来一次吧")
    index = index+1
if temp == random:
    print("我草，你是我肚子里的蛔虫么。这么厉害")
    print("答对也没有奖品额")
    print("拜拜，不玩了")
if index == 3:
    print("太笨了。三次已到，不玩了，拜拜")

