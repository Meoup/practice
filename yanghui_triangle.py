# 输出如下图
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]

def gene(n):
    lis = [1]
    i = 1
    while True:
        yield lis
        lis = [lis[x] + lis[x + 1] for x in range(len(lis) - 1)]
        lis.insert(0, 1)
        lis.append(1)
        i += 1
        if i > n:
            break
generator = gene(12)
for j in generator:
    print(j)
