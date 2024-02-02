# 列表推导式
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 字典推导式
dic = {x: x % 3 for x in range(10)}
print(dic)

# 集合推导式
sites = {x for x in "aslafkjnafg;n;" if x not in "abcd"}
print(sites)

# 元组推导式
tuples = (x for x in range(10))
print(tuples)
a = tuple(tuples)
print(a)
