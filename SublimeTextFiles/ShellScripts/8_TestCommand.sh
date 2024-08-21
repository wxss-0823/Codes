# 使用 test 做数值判断
num1=34
num2=27

# 注意此时不能有括号
if test $[num1*num2] -eq $[num2*num1]
then
	echo "The commutative law of multiplication is true"
else
	echo "The commutative law of multiplication is false"
fi

# 使用 test 做字符串判断
str1="wxss"
str2="wangxishengshun"

if test ${str1} = ${str2}
then
	echo "str1 is equal to str2"
else
	echo "str1 is not equal to str2"
fi

# 使用 test 做文件判断
if test -e ./EchoCommand.txt
then
	echo "TRUE"
else
	echo "FALSE"
fi

# 数值计算的两种等价形式
result=$[num1+num2]
echo -e "${result} \c"
result=`expr $num1 + $num2`
echo ${result}