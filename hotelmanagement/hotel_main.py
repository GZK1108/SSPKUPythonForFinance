from rooms_tools import *
import time

while True:
    show_menu()
    action = input("请选择操作：")
    print(f"您选择的操作是：{action}")
    if action == "1":
        new_room()
    elif action == "2":
        show_all()
    elif action == "3":
        search_room()
    elif action == "0":
        print("欢迎再次使用【酒店管理系统】")
        break
    else:
        print("输入有误，请重新输入")
    # 暂停3秒
    time.sleep(1)
