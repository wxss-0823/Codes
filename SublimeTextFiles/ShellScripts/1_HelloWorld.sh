#!/bin/bash

echo "Hello World !"

# 变量赋值
file='d/Program Files'
# 打印需要使用 $ 标明
echo ${file}

# 将路径下的文件赋给 files 并依次打印
for files in `ls /d/'Program Files'`;do
	echo ${files}
done