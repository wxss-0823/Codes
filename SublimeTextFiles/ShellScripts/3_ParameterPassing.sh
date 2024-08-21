#!/bin/bash

echo "Shell 传递参数实例！"
echo "第一个参数: $1"
echo "第二个参数: $2"
echo "第三个参数: $3"

# 传递参数 * 和 @ 的区别
echo "Shell 传递参数实例！"
echo "第一个参数: $1"
echo "一共传递了 $# 个参数"

echo "参数分别为: $*"
echo "参数分别为: $@"

# 区别演示
echo "-- \$* 演示 --"
for i in "$*";do
	echo ${i}
done

echo "-- \$@ 演示 --"
for i in "$@";do
	echo ${i}
done