local r = require "luasql.mysql"

--创建环境对象
local env = r.mysql()

--连接数据库
local conn = env:connect("wxss","root","020823","localhost",3306)

print("Connection successfully!")

local cur = conn:execute("select curdate();")

result = cur:fetch({}, "a")

print(result["curdate()"])

conn:close()  --关闭数据库连接
env:close()   --关闭数据库环境