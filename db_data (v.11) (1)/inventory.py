# 체크
def check(message, start, end):
    if message in list(map(str, range(start, end + 1))):
        message = int(message)
        return message
    else:
        return message

# 아이템 프린트 2
def item_print_2(item):
    if item.use == 'item':
        print(f"이름 : {item.name}\n설명 : {item.explanation}")
    elif item.use == 'main' or item.use == 'sub':
        print(f"이름 : {item.name}\n설명 : {item.explanation}\n분류 : {item.system}\n쿨타임 : {item.cool_time}\n사용 가능 횟수{item.count}\n(다 읽으셨다면 enter.)")
        input()

# 아이템 프린트 1
def item_print_1(player_1, ans):
    while True:
        item_print_2(item[ans])
        if item.use == item:
            ans_1 = input(f"{item[ans].name}을(를) 사용하시겟습니까? (y / n) : ")
            if ans_1 == "y":

                item[ans].count -= 1
                if item[ans].count <= 0:
                    del item[ans]
                return player_1
            elif ans_1 == "n":
                break
            else:
                print("올바른 문자를 입력하세요")

# 인벤토리 출력
def inventory(player_1, ans):
    while True:
        ans_1 = change(ans)
        print(f"{str(ans_1) + ' 인벤토리 ':=^25}")
        print(f"{'Num': ^12}{'Name': ^12}")
        if len(player_1.inven[ans]) == 0:
            print(f"{'없음': ^12}{'없음': ^12}")
        if ans == 'main' or ans == 'sub':
            for i in range(len(player_1.inven[ans])):
                print(f"{i + 1: ^12}{player_1.inven[ans][i].name: ^12}")
        else:
            for i in range(len(player_1.inven[ans])):
                print(f"{i + 1: ^12}{player_1.inven[ans][i].name}  x{str(player_1.inven[ans][i].count): ^12}")
        if ans == 'main' or ans == 'sub':
            ans_2 = input("\n해당 무공의 정보를 보고 싶다면 해당 무공의 번호를 입력하세요\n나가려면 (enter)\n:")
        else:
            ans_2 = input("\n아이템의 정보를 보고 싶다면 해당 아이템의 번호를 입력하세요\n나가려면 (enter)\n:")
        ans_2 = check(ans_2, 1, len(player_1.inven[ans]))
        if type(ans_2) == type(0):
            ans_2 -= 1
            if ans == 'item':
                print("\n{0:=^25}".format("Num" + str(ans_2) + " 정보"))
                item_print_1(player_1, ans)
            else:
                print("\n{0:=^25}".format("Num" + str(ans_2) + " 정보"))
                item_print_2(ans)
        elif ans_2 == "":
            break
        else:
            print("올바른 숫자를 입력하세요")


# 무술 인벤토리 프린트
def martial_arts_inventory_print(player_1, ans):
    print("\n" * 38)
    if ans == 'q':
        print(f"{' 장착중인 메인 무공 ':=^25}")
        player_1.m_martial_arts_equipment()
        inventory(player_1, 'main')
    elif ans == 'w':
        print(f"{' 장착중인 서브 무공 ':=^25}")
        player_1.s_martial_arts_equipment()
        inventory(player_1, 'sub')


# 무술 인벤토리
def martial_arts_inventory(player_1):
    while True:
        print("\n" * 38)
        print("인벤토리를 선택하세요 [메인 무공 (q) /서브 무공 (w)]")
        ans = input("나가려면 (enter) = ")
        if ans == "q" or ans == "w":
            martial_arts_inventory_print(player_1, ans)
        elif ans == "":
            break
        else:
            print("올바른 문자를 입력하세요")

# 바꾸기
def change(ans):
    if ans == 'item':
        return '아이템'
    elif ans == 'main':
        return '메인 무공'
    elif ans == 'sub':
        return "보조 무공"