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

# 列表推导式实例
names = [
    'Homer J Simpson',
    'Marge H Bouvier',
    'Alejandro Johnny Wilson'
]
last_name = [name.split(" ")[-1] for name in names]
print(last_name)

# 列表解包
data = [
    'Homer',
    'Simpson',
    'Husband',
    'Lazy',
    43
]
first_name, last_name, *_, age = data
print(f"{first_name} {last_name}'s age is {age}")