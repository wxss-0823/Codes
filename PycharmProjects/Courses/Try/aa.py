# 基于用户的协同过滤算法

# 初始数据
user_item_dict = {"A": ['a', 'b', 'e'],
                  "B": ['c', 'e', 'g'],
                  "C": ['a', 'd', 'f', 'g'],
                  "D": ['b', 'c', 'e', 'f'],
                  "E": ['b', 'd'],
                  "F": ['c', 'd', 'f']
                  }


class UserCF:
    def __init__(self, User_item_dict):
        print (user_item_dict)
        # 将每个用户的物品取集合
        self.user_matrix = None
        self.user_item_dict = {key: set(User_item_dict[key]) for key in User_item_dict.keys()}
        # 用户列表
        self.users_list = list(self.user_item_dict.keys())
        print(self.users_list)

    # 两两用户之间计算用户相似度
    def compute_similer_twouser(self):
        # 记录与其他用户相似度的字典
        user_similer_list = dict()

        for i in self.users_list:
            user_similer_list[i] = dict()
            for j in self.users_list:
                # 去除自身相似度
                if i != j:
                    # 两用户间物品并集，并计算余弦相似度
                    similer_item = self.user_item_dict[i] & self.user_item_dict[j]
                    user_similer_list[i][j] = round(
                        len(similer_item) / (len(self.user_item_dict[i]) * len(self.user_item_dict[j])) ** 0.5, 3)
        return user_similer_list

    #     优化后的倒查表方式计算用户相似度
    def computer_similer_backform_normal(self):
        import numpy as np
        # 记录物品的所有用户的字典
        item_user_dict = dict()
        # 建立物品到用户的倒查表
        for i, items in self.user_item_dict.items():
            for j in items:
                if j not in item_user_dict.keys():
                    item_user_dict[j] = list()
                item_user_dict[j].append(i)

        # 建立用户物品二维矩阵
        user_matrix = np.zeros((len(self.users_list), len(self.users_list)), dtype=int)
        for item, users in item_user_dict.items():
            for user1 in users:
                for user2 in users:
                    if user1 != user2:
                        # 记录不同用户间共同物品的数目
                        user_matrix[self.users_list.index(user1)][self.users_list.index(user2)] += 1

        # 计算用户相似度
        user_similer_list = dict()
        for user1 in self.users_list:
            user_similer_list[user1] = dict()
            for user2 in self.users_list:
                if user1 != user2:
                    # 利用二维矩阵存储的用户相似度进行计算
                    user_similer_list[user1][user2] = round(
                        user_matrix[self.users_list.index(user1)][self.users_list.index(user2)] /
                        (len(self.user_item_dict[user1]) * len(self.user_item_dict[user2])) ** 0.5, 3)
        return user_similer_list

    # 惩罚热门物品和倒查表方式计算用户相似度（同倒查表方式一致，只是在相似度计算中引入惩罚））
    def computer_similer_backform_punish(self):
        import numpy as np
        import math
        item_user_dict = dict()
        # 建立物品到用户的倒查表
        for i, items in self.user_item_dict.items():
            for j in items:
                if j not in item_user_dict.keys():
                    item_user_dict[j] = list()
                item_user_dict[j].append(i)

        # 建立用户矩阵
        self.user_matrix = np.zeros((len(self.users_list), len(self.users_list)))
        for item, users in item_user_dict.items():
            for user1 in users:
                for user2 in users:
                    if user1 != user2:
                        # 对热门物品进行惩罚
                        self.user_matrix[self.users_list.index(user1)][self.users_list.index(user2)] += 1 / math.log(
                            1 + len(users))

        # 计算用户相似度
        user_similer_list = dict()
        for user1 in self.users_list:
            user_similer_list[user1] = dict()
            for user2 in self.users_list:
                if user1 != user2:
                    user_similer_list[user1][user2] = round(
                        self.user_matrix[self.users_list.index(user1)][self.users_list.index(user2)] /
                        (len(self.user_item_dict[user1]) * len(self.user_item_dict[user2])) ** 0.5, 3)
                    self.user_matrix[self.users_list.index(user1)][self.users_list.index(user2)] = \
                        user_similer_list[user1][user2]
        return user_similer_list, item_user_dict

    # 计算指定用户的推荐物品
    def compute_interest_item(self, user):
        import numpy as np
        user_similer_list, item_user_dict = self.computer_similer_backform_punish()
        # 本处相似用户集合大小为3，取相似度高的前三名用户
        sort_coor = np.argsort(self.user_matrix[self.users_list.index(user)])[::-1][:3]

        recommend_item = dict()
        for item in item_user_dict.keys():
            recommend_item[item] = 0
            for i in sort_coor:
                # 推荐不在指定用户物品集中，但在相似用户物品集中的物品，r=1
                if item not in self.user_item_dict[user] and item in self.user_item_dict[self.users_list[i]]:
                    recommend_item[item] += self.user_matrix[self.users_list.index(user)][i]

        # 对推荐的物品按照感兴趣程度降序
        recommend_item = {k: v for k, v in sorted(recommend_item.items(), key=lambda Item: Item[1], reverse=True) if
                          v >= 0.5}
        return list(recommend_item.keys())


usercf = UserCF(user_item_dict)
print('两两用户之间计算用户相似度:')
print(usercf.compute_similer_twouser())
print('优化后的倒查表方式计算用户相似度:')
print(usercf.computer_similer_backform_normal())
print('惩罚热门物品和倒查表方式计算用户相似度:')
print(usercf.computer_similer_backform_punish()[0])
print('推荐物品:')
print(usercf.compute_interest_item('A'))
