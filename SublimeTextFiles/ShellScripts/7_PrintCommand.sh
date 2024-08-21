# format-string 为双引号
printf "%d %s\n" 1 "abc"

# format-string 为单引号
printf '%d %s\n' 1 "abc"

# format-string 没有引号
printf "%d\n" 1

# format-string 仅指定了一个参数，超出的参数仍会按照前面的格式输出
printf "%d %d %d\n" 1 2 3 4 5 6 7 8 9

# 如果没有声明，%s 用 null ，%d 用 0
printf "%s and %d \n"

# 输出字符串 \n
printf "%s\n" "A\nB"
# 输出二进制数 \n
printf "%b\n" "A\nB"