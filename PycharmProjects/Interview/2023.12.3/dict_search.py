while True:
    Key = input("输入：\n")
    Dict = {'a': '1', 'b': '2'}
    '''
    if Key in Dict:
        print('Output:', Dict.get(Key))
    else:
        print('Key is not in the Dict!')
    '''
    print(Dict.get(Key, 'Key is not in the Dict'))
