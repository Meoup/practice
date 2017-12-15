"""递归函数"""

# 实现n的阶乘
# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
# 这是一个递归函数
# print(fact(6))

# 请编写move(n, a, b, c)函数，输出为汉诺塔游戏的步骤

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, "a", "b", "c")
