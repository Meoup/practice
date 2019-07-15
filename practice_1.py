# -*- coding:utf-8 -*-

#给定一个只包含字母的string,返回单个字母出现的次数
string = 'congratulations'
dic = {}
for i in string:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
print(dic)
