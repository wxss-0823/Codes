def AddStuID():
    file = open(".\\logs.txt", "a")
    while True:
        name, age, weight, grade = input("Please Input the name, age, weight and grade. "
                                         "Specialized everyone with \"space\":").split()
        information = [name, age, weight, grade]
        output = ' '.join(information)
        file.writelines(output + '\n')
        ex = input("Print exit to exit?")
        if ex == 'exit':
            file.close()
            break
        else:
            continue
    return


def Search(moder):
    fp = open(".\\logs.txt", "r+")
    NameDict = {}
    Search_mode = ['name', 'age', "weight", "grade"]
    lines = fp.readlines()
    for item in lines:
        items = item.split()
        NameDict[items[moder - 1]] = [items[moder % 4], items[(moder + 1) % 4], items[(moder + 2) % 4]]
    while True:
        search_mode_name = input(f"Print {Search_mode[moder - 1]} to search:")
        if search_mode_name in NameDict:
            print(
                f"{Search_mode[moder % 4]}:{NameDict[search_mode_name][0]}, "
                f"{Search_mode[(moder + 1) % 4]}:{NameDict[search_mode_name][1]},"
                f" {Search_mode[(moder + 2) % 4]}:{NameDict[search_mode_name][2]}")
        elif search_mode_name == "exit":
            break
        else:
            print(f"No match {Search_mode[moder - 1]}, check your {Search_mode[moder - 1]}")
            if input("Print exit to exit.\n") == "exit":
                break
    return


if __name__ == '__main__':
    while True:
        print("1.Add Students Information.")
        print("2.Search Existed Student Information")
        print("Print exit to exit.")
        Condition = input()
        while True:
            if Condition == "1":
                AddStuID()
            elif Condition == "2":
                print("How to search?")
                print("1.Search in name.")
                print("2.Search in age.")
                print("3.Search in weight.")
                print("4.Search in grade.")
                print("Print exit to exit.")
                mode = input()
                if mode == "1" or mode == "2" or mode == "3" or mode == "4":
                    Search(int(mode))
                elif mode == "exit":
                    break
                else:
                    print("Please check your input!")
                    print("If you want to exit?")
                    while input() == "exit":
                        break
            elif Condition == "exit":
                exit()
            else:
                print("Please check your input, if you want to exit? Print exit to exit")
                while input() == "exit":
                    break




