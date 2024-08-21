# show string
echo "xxxx"

# show escape string
echo "\"xxx\""

# show variables
read name
echo "$name is a test"

# show enter
# -e open escape mode
echo -e "xxx \n"
echo "xxxx"

# show not enter
echo -e "xxx \c"
echo "xxxx"

# show diectional to specific file
echo "xxx" > EchoCommand.txt

# show output as-is
echo 'xxx% \n" "'

# show result of command
echo `date`