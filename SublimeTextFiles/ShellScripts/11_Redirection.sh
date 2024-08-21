# 重定向输出流
echo "wxss" >> ./EchoCommand.txt

# 重定向输入流
read string < ./EchoCommand.txt
echo "$string"

# Here document
wc -l << delimeter >> ./EchoCommand.txt
`cat ./EchoCommand.txt`
delimeter