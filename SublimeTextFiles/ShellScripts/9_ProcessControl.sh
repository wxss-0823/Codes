# if-else 控制
IF_ELSE()
{
	# 内部的 $1 $2 描述传入参数的数量
	if (( $1 == $2 ))		# 等价于 if [ $1 == $2 ]
	then
		echo "$1 = $1"
	elif (( $1 > $2 ))		# 等价于 if [ $1 -gt $2 ]
	then
		echo "$1 > $2"
	elif (( $1 < $2 ))		# 等价于 if [ $1 -lt $2 ]
	then
		echo "$1 < $2"
	else
		echo "没有符合的选项"
	fi
}

# for 控制
FOR()
{
	for loop in 1 2 3 4 5
	do
		echo “The value is: $loop”
	done
}

# while 控制
WHILE()
{
	i=$1
	while (( i < $2 ))
	do
		echo "${i} < $2"
		((i++))
	done
}

# until 控制
UNTIL()
{
	a=$1
	until [ ! $a -lt 10 ]
	do 
		echo "$a"
		a=`expr $a + 1`
	done
}

# case-esac 控制
CASE()
{
	while true
	do
		read cases
		case $cases in
			"wxss") echo "wxss"
			;;
			"wangxishengshun") echo "wangxishengshun"
			;;
			"exit") 
				echo "Goodbye!"
				break
			;;
			*) 
				echo "no match"
			;;
		esac
	done
}

# 执行 if-else 控制
# IF_ELSE $1 $2 				# 外部的 $1 $2 表示传入函数的第一个参数是终端运行是传入的参数

# 执行 for 控制
# FOR

# 执行 while 控制
# WHILE $1 $2

# 执行 until 控制
# UNTIL $1

# 执行 case 控制
# CASE