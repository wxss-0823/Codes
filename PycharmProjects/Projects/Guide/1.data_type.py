# 变量赋值
a, b, c = 1, 2, "wxss"
print(a, b, c)
# 判断类型
print(type(a))


class A:
  pass


class B(A):
  pass


# type 不认为子类是父类类型
print(type(B()) == A)
# isinstance 认为子类是父类类型
print(isinstance(B(), A))

# 创建集合
sites = {"a", "b"}
sites.update((1, 2))
sites.add((1, 2))
print(sites)

# 创建二进制数据
x = b"hello"
print(x[0] == "h")
print(x[0] == ord("h"))
