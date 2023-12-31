import numpy as np

i = 0
xiaoming_dict = {}
knowledge = ['语文', '数学', '英语']
value = {[1, 1, 1], [2, 2, 2], [3, 3, 3]}
knowledge_nums = np.array(knowledge)
value_num = np.array(value)
for i in range(len(knowledge)):
    xiaoming_dict[knowledge_nums[i]] = list(value_num[i])
print(xiaoming_dict)
# {'数学': 60, '语文': 60, '英语': 60}
