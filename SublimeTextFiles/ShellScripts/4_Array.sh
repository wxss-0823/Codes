# 创建一个数组
basic_info=(wxss 22 183)
# 创建一个关联数组
declare -A basic_dict
basic_dict["name"]="wangxishengshun"
basic_dict["age"]=21
basic_dict["height"]=183

# 访问数组
echo ${basic_info[0]}
echo ${basic_dict["age"]}

# 获取数组长度
echo ${#basic_info[*]}
echo ${#basic_dict[@]}