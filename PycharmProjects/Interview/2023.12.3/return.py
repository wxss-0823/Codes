def return_1(r):
    print('return 1')
    return r ** 2


if __name__ == '__main__':
    dicts = [1, 2, 3, 4, 5, 6]
    len_dicts = len(dicts)
    for i in range(len_dicts):
        return_main = return_1(i)
        print(return_main)
