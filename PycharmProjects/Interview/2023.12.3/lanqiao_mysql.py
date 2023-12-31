import pymysql

# 数据库链接信息
db = pymysql.connect(host='localhost',
                     user='root', database='lanqiao')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 查询语句，查询user表
sql = 'show tables '

# 执行sql语句查询
cursor.execute(sql)

# 获取数据
rest = cursor.fetchall()

# 查找内容
content = ()
tables = []
for i in range(len(rest) - 1):
    tables.append(rest[i])
    # tables = ['lanqiao0a0c8f43','lanqiao0a76e274','lanqiao1070f68d',
    # 'lanqiao19c74f0d','lanqiao249809e6','lanqiao3dd32580','
    # lanqiao5e7ee950','lanqiao9fc332d9','lanqiaob2704129','
    # lanqiaod68c5aad']
for i in range(len(tables)):
    sql = 'select * from %s' % (tables[i])
    char = cursor.execute(sql)
    if char != 0:
        target = tables[i]

# 取出键值
sql = 'select lanqiao_key from %s' % target
cursor.execute(sql)
key = cursor.fetchone()
k = open('key.txt', 'w')
k.write(key[0])
