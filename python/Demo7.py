# 定义一个求和函数
def calcSum(beg,end = 2):
    theSum = 0
    for i in range(beg,end + 1):
        theSum += i
    print(theSum)

# 函数调用
calcSum(1,100)
calcSum(300,400)
calcSum(500,1000)