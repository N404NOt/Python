# # 控制台输入
#
# num = input('请输入一个整数: ')
# print(type(num))
# print(f'您输入的数字是 {num}')
#
# # num 是 str 类型
import random
import sys

aaa = input('请输入第一个整数')
b = input('请输入第二个整数')

aaa = int(aaa)
b = int(b)
# str() float()
print(f'a + b  = {aaa + b}')

for i in range(0,10) :
    print(f'当前为{i}')

point = random.randint(1,10)
sys.exit(0)
# 暂停一秒
time.sleep(1)

