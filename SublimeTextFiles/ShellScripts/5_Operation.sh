# 算数运算符 + - * / % = == !=
ArithmeticOperators()
{
	echo "---------- ArithmeticOperators ----------"

	a=10
	b=20

	val=`expr $a + $b`
	echo "$a + $b = ${val}"

	val=`expr $a - $b`
	echo "$a - $b = ${val}"

	val=`expr $a \* $b`
	echo "$a * $b = ${val}"

	val=`expr $b / $a`
	echo "$b / $a = ${val}"

	val=`expr $b % $a`
	echo "$b % $a = ${val}"

	val=`expr $a == $b`
	if [ ${val} == 1 ]
	then
		echo "$a equals to $b is true"
	else 
		echo "$a equals to $b is false"
	fi

	val=`expr $a != $b`
	if [ ${val} == 1 ]
	then
		echo "$a equals to $b is false"
	else 
		echo "$a equals to $b is true"
	fi

	if [ $a == $b ]
	then
		echo "$a is equal to $b"
	else 
		echo "$a is not equal to $b"
	fi

	echo "----------         End         ----------"
}

# 关系运算符 -eq -ne -gt -lt -ge -le
RelationalOperators()
{
	echo "---------- RelationalOperators ----------"

	a=10
	b=20
	if [ $a -eq $b ]
	then
		echo "$a is equal to $b"
	else
		echo "$a is not equal to $b"
	fi

	if [ $a -ne $b ]
	then 
		echo "$a is not equal to $b"
	else
		echo "$a is equal to $b"
	fi

	if [ $a -gt $b ]
	then
		echo "$a is greater than $b"
	else
		echo "$a is less than or equal to $b"
	fi

	if [ $a -lt $b ]
	then
		echo "$a is less than $b"
	else
		echo "$a is greater than or equal to $b"
	fi

	if [ $a -ge $b ]
	then
		echo "$a is greater than or equal to $b"
	else
		echo "$a is less than $b"
	fi

	if [ $a -le $b ]
	then
		echo "$a is less than or equal to $b"
	else
		echo "$a is greater than $b"
	fi

	echo "----------         End         ----------"
}

# Boolean运算符 ！ -o -a
BooleanOperators()
{
	echo "----------   BooleanOperators  ----------"

	a=7
	b=15

	if [ $a != $b ]
	then
		echo "$a is not equal to $b"
	else
		echo "$a is equal to $b"
	fi

	if [ $a -lt 10 -o $a -gt 20 ]
	then
		echo "$a is less than 10 or greater than 20"
	else
		echo "$a is between 10 and 20"
	fi

	if [ $b -gt 10 -a $b -lt 20 ]
	then
		echo "$b is greater than 10 and less than 20"	
	else
		echo "$b is not between 10 and 20"
	fi

	echo "----------         End         ----------"
}

# 逻辑运算符 && ||
LogicOperators()
{
	echo "----------    LogicOperators   ----------"

	a=10
	b=20

	# 这里需要加两个中括号
	if [[ $a -lt 100 && $b -gt 100 ]]
	then
		echo "return true"
	else
		echo "return false"
	fi

	if [[ $a -lt 100 || $b -gt 100 ]]
	then
		echo "return true"
	else
		echo "return false"
	fi

	echo "----------         End         ----------"

}

# 文件测试运算符
FileTestingOperators()
{
	echo "---------- FileTestingOperators ---------"

	file="./1_HelloWorld.sh"
	if [ -r $file ]
	then
		echo "$file can be read"
	else
		echo "$file can not be read"
	fi

	if [ -e $file ]
	then
		echo "$file is exist"
	else
		echo "$file is not exist"
	fi

	if [ -w $file ]
	then
		echo "$file can be written"
	else
		echo "$file can not be written"
	fi

	echo "----------         End          ---------"
}
# 运行算数运算符函数
# ArithmeticOperators

# 运行关系运算符函数
# RelationalOperators

# 运行布尔运算符函数
# BooleanOperators

# 运行逻辑运算函数
# LogicOperators

# 运行文件测试函数
FileTestingOperators