# 新建一个用于存储酒店信息的列表
class Room:
    def __init__(self, room_id, room_type, room_price, room_status):
        self.room_id = room_id
        self.room_type = room_type
        self.room_price = room_price
        self.room_status = room_status


rooms = {}  # 房间信息，键为房间号，值为房间对象
rooms_types = ["单人间", "双人间", "三人间", "大床房", "豪华间"]
# 键值对，键为房间号，值为房间对象


def show_menu():
    print("*" * 50)
    print("\t 欢迎使用【酒店管理系统】V1.0")
    print("\t\t  1. 添加房间")
    print("\t\t  2. 显示全部")
    print("\t\t  3. 查询房间")
    print("\t\t  0. 退出系统")
    print("*" * 50)


def new_room():
    print("==========添加房间==========")

    room_id = input("请输入房间号（四位：如0001）：")
    # 类型检测，要求房间号为四位数字
    if not room_id.isdigit() or len(room_id) != 4:
        print("房间号输入有误，请重新输入")
        return new_room()
    if room_id in rooms.keys():
        print("房间号已存在，请重新输入")
        return new_room()

    types_info = [f"{i + 1}：{rooms_types[i]}" for i in range(len(rooms_types))]
    room_type = input(f"请选择房间类型：{','.join(types_info)}：")
    if not room_type.isdigit() or int(room_type) not in range(len(rooms_types)):
        print("房间类型输入有误，请重新输入")
        return new_room()
    room_type = rooms_types[int(room_type) - 1]

    room_price = input("请输入房间价格：")
    try:
        room_price = float(room_price) if float(room_price) > 0 else 0
    except ValueError:
        print("房间价格输入有误，请重新输入")
        return new_room()

    room_status = input("请输入房间状态：1：满，0：空：")
    if room_status not in ["1", "0"]:
        print("房间状态输入有误，请重新输入")
        return new_room()
    room_status = "满" if room_status == "1" else "空"
    room = Room(room_id, room_type, room_price, room_status)
    rooms[room_id] = room
    print("添加成功")


def show_all():
    print("==========显示全部==========")
    # 按照房间号升序排列
    rooms_sorted_id = sorted(rooms.keys())
    for room_id in rooms_sorted_id:
        room = rooms[room_id]
        print(f"房间号：{room.room_id}，房间类型：{room.room_type}，房间价格：{room.room_price}，房间状态：{room.room_status}")
    print(f"共有房间{len(rooms)}间")
    input("按任意键返回")


def modify_room(room_id):
    room = rooms[room_id]
    types_info = [f"{i + 1}：{rooms_types[i]}" for i in range(len(rooms_types))]
    room_type = input(f"请选择房间类型：{','.join(types_info)}：")
    if not room_type.isdigit() or int(room_type) not in range(len(rooms_types)):
        print("房间类型输入有误，请重新输入")
        return modify_room(room_id)
    room.room_type = rooms_types[int(room_type) - 1]

    room_price = input("请输入房间价格：")
    try:
        room_price = float(room_price) if float(room_price) > 0 else 0
    except ValueError:
        print("房间价格输入有误，请重新输入")
        return modify_room(room_id)
    room.room_price = room_price

    room_status = input("请输入房间状态：1：满，0：空：")
    if room_status not in ["1", "0"]:
        print("房间状态输入有误，请重新输入")
        return modify_room(room_id)
    room.room_status = "满" if room_status == "1" else "空"
    print("修改成功")


def search_room():
    print("==========查询房间==========")
    room_id = input("请输入要查询的房间号：")
    room = rooms.get(room_id, None)
    if room:
        print(f"房间号：{room.room_id}，房间类型：{room.room_type}，房间价格：{room.room_price}，房间状态：{room.room_status}")
        action = input("请选择操作：1：修改，2：删除，0：返回，其他：退出：")
        if action == "1":
            modify_room(room_id)
        elif action == "2":
            del rooms[room_id]
            print("删除成功")
        elif action == "0":
            return search_room()
    else:
        print("房间不存在")
    input("按任意键返回")


def file_write():
    with open("rooms.txt", "w", encoding="utf-8") as f:
        for room_id, room in rooms.items():
            f.write(f"{room_id},{room.room_type},{room.room_price},{room.room_status}\n")


def file_read():
    with open("rooms.txt", "r", encoding="utf-8") as f:
        for line in f:
            room_id, room_type, room_price, room_status = line.strip().split(",")
            room = Room(room_id, room_type, float(room_price), room_status)
            rooms[room_id] = room
