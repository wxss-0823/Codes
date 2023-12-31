# coding=utf-8
# 特征选取与计算

from copy import copy
from tmall import *


# 特征计算
# 基于逻辑回归的推荐需要划分训练集与预测集
# 将前2个月的交互划分为训练集 train
# 将后2个月的交互划分为
# 通过参数classify进行判断，不处理与当前类型不符合的数据。
def generateFeature(classify, data):
    # 存储用户特征
    F = {}

    # 所有要进行统计的特征，在这里进行声明并赋予初始值
    item = {
        'click': 0,  # 点击次数
        'buy': 0,  # 购买次数
        'fav': 0,  # 加入收藏夹次数
        'cart': 0,  # 加入购物车次数
        'diff_day': 1000,  # 因为是要推测下一个月的购买情况
        # 显然在最近一段时间有交互的，购买可能性越大
        # 因此将最后一次交互的相差天数也作为一个特征
        # 如我们推测7月15-8月15这一个月的购买情况，用户在7月8号跟7月12号均有交互记录
        # 则diff_day为3（取最近的7月12，计算跟7月15的相差天数）
        # 此处可添加其他特征

    }

    # 计算复杂的特征时，上面定义的item中可能会有一些中间特征
    # 所以需要指定只用于逻辑回归的特征
    feature_name = ['click', 'buy', 'fav', 'cart', 'diff_day', 'normalization']

    power_ave = 0
    # 1. 计算用户特征
    for uid, bid, action_type, month, day in data:
        # 首先通过日期判断判断该条数据符合当前要生成的特征集类型
        # 如果不符合，则跳过该条数据
        if classify != getClassify(month, day):
            continue

        # 初始化
        F.setdefault(uid, {})
        F[uid].setdefault(bid, copy(item))

        # 新建一个引用，简化代码
        e = F[uid][bid]

        # 基础特征计算
        if action_type == 0:
            e['click'] += 1
        elif action_type == 1:
            e['buy'] += 1
        elif action_type == 2:
            e['fav'] += 1
        elif action_type == 3:
            e['cart'] += 1

        # 时间特征
        diff_day = getDiffDayByClass(classify, (month, day))
        if diff_day < e['diff_day']:
            e['diff_day'] = diff_day

    # 计算其他特征
        e['power_ave'] = e['click'] + e['buy'] + e['cart']
        if power_ave < e['power_ave']:
            power_ave = e['power_ave']
        # 归一化
        e['normalization'] = e['power_ave'] / power_ave

    return F, feature_name
