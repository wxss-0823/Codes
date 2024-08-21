# 定义一个函数 加法器
Add()
{
	sum=$(($1 + $2))
	echo "实际的返回值：$sum"
	# 做非越界处理
	return `expr $sum % 255`
}

# 调用函数
Add 334 553
echo "越界的返回值：$?"
