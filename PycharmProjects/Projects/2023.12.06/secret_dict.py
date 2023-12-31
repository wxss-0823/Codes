import itertools as its

words = "12"  # 可选择的字符
r = its.product(words, repeat=8)  # 组成8位字符串
dic = open("pwd8.txt", "a")  # 存储为wifi密码字典
# wifi密码完成换行，并写入txt文档
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()
