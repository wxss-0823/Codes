local r = require "luasql.mysql"

--创建环境对象
local env = r.mysql()

--连接数据库
local conn = env:connect("wxss","root","020823","localhost",3306)

print("Connection successfully!")

local cur = conn:execute("select curdate();")

local result = cur:fetch({}, "a")

print(result["curdate()"])

local cur = conn:execute("select * from users;")

while result do 
    result = cur:fetch(result, "a")
    if result ~= nil then
        for index, value in pairs(result) do
        print(index .. ": " .. value)
        end
    end
end

cur:close()   --关闭数据库指针
conn:close()  --关闭数据库连接
env:close()   --关闭数据库环境