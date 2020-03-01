from random import choice
from random import randint
import time

print("\nthe Martial Arts RPG game project\n")

# 체크
def check(message, start, end):
    if message in list(map(str, range(start, end + 1))):
        message = int(message)
        return message
    else:
        return message

# 플레이어 클래스
class Player:
    def __init__(self, name, Arena, point, health, M_martial_arts_equipment, S_martial_arts_equipment, inven, money, liv, exp):
        self.name = name
        self.Arena = Arena
        self.point = point
        self.health = health
        self.M_martial_arts_equipment = {"M_martial_arts_1": ["없음"], "M_martial_arts_2": ["없음"], "M_martial_arts_3": ["없음"], "M_martial_arts_4": ["없음"]}
        self.S_martial_arts_equipment = {"s_martial_arts_1": ["없음"], "s_martial_arts_2": ["없음"]}
        self.inven = {"main_martial_arts": [], "sub_martial_arts": [], "item": []}
        self.money = money
        self.liv = liv
        self.exp = exp

    # 현재 상태 확인
    def showinfo(self):
        print(f"{'나의 상태':=^25}\n이름 : {self.name}\n레벨 : {self.liv}\n아레나 / 점수 : {self.Arena}{self.health}\n돈 : {self.money}")

    # 전투중 상태 확인
    def F_showinfo(self):
        print(f"{'나의 상태':=^25}\n이름 : {self.name}\n체력 : {self.health}")
        if len(self.M_martial_arts_equipment['M_martial_arts_1']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_2']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_2'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_2'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_3']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_3'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_3'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_4']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_4'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_4'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_1']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_2']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_2'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_2'][0]}")

    # 장착 무술 보기
    def martial_arts_equipment(self):
        if len(self.M_martial_arts_equipment['M_martial_arts_1']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_2']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_2'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_2'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_3']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_3'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_3'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_4']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_4'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_4'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_1']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_2']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_2'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_2'][0]}")

# 메인
def main():
    input("게임을 시작하려면 엔터")

    print("\n" * 38)

    try:
        import save
    except:

        player_name = input("\n플레이어 이름을 입력하십시오. = ")
        while player_name == "":
            print("\n유효한 이름을 입력하십시오")
            player_name = input("플레이어 이름을 입력하십시오. = ")
        player_1 = Player(player_name, 1, 0, 100, [], [], [], 0, 0, 0)

        po_count = 0
        ag_count = 0
        ad_count = 0

        plag = 0

    time.sleep(1.3)
    print('\n' * 2)
    print("정상적으로 로그인 되었습니다.")
    time.sleep(0.7)
    print("정보 불러오는 중...")
    time.sleep(0.7)
    print("환영합니다." + player_name + "님")
    time.sleep(1)

    while True:

        print("\n" * 38)

        turn_chack(self, player_x, player_y, plag)  # 아레나, 스텟(레벨)

        player_1.showinfo()

        print("{0} : {1}/{2}/{3}".format( \
            '나의스텟 (힘, 민첩, 모험)', po_count, ag_count, ad_count))

        if plag == 0:
            print("\n도움을 원한다면 'h' 입력")

        ans = input("\n무엇을 하시겠습니까? : ")

        if ans == "q":

        elif ans == "e":
            martial_arts_equipment(self)
        elif ans == "r":
            inventory(self)
            continue
        elif ans == "t":
            showshop(self)
            continue
        elif ans == "a":
            print("\n게임설명\n전투시작 : q\n무술 장착 및 해제 : e\n인벤토리 : r\n상점 : t\n도움말 : a\n게임종료 : p\n한국어를 웬만하면 누르지 마세요.(버그의 원인이 됩니다.)\n다 읽으셨다면 enter.")
            input()
        elif ans == "p":
            game_over()
        else:
            print("다시 입력해 주십시오")

        plag += 1

if __name__ == "__main__":
    main()