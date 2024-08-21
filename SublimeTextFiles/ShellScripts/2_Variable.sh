#!/bin/bash

# 定义不同类型的变量
my_string="wangxishengshun"  # 定义字符串
echo ${my_string}

declare -i my_integer=22	 # 定义整型
echo ${my_integer}

my_array=(1 2 3 4 5)		 # 定义数组
echo ${my_array[@]}

declare -A associative_array	# 定义关联型
associative_array["name"]="wxss"
associative_array["age"]=21		# 可以保存不同类型
# echo ${associative_array["name"]}
echo ${associative_array[*]}

echo ${PATH}				 # 环境变量
echo $0						 # 特殊保留变量

# 获取字符串长度
echo ${#my_string}				# 等价于 echo ${#my_string[0]}
# 提取子字符串
echo ${my_string1:4}

# 查找字符串
string="Google is a good website!"
echo `expr index "${string}" a`

# 获取数组长度
echo ${#my_array[*]}
echo ${#my_array[@]}
# 获取单个元素的长度
echo ${#my_array[0]}

# 多行注释
: '
这是注释的部分。
可以有多行内容。
'