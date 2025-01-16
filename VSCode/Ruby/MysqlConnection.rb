$LOAD_PATH << 'D:/Users/ProjectFiles/Codes/VSCode/Ruby'
require 'mysql2'
client = Mysql2::Client.new(
    :host     => '127.0.0.1', # 主机
    :username => 'root',      # 用户名
    :password => '020823',    # 密码
    :database => 'wxss',      # 数据库
    :encoding => 'utf8'       # 编码
    )

results = client.query("SELECT VERSION()")
results.each do |row|
    puts row
end
