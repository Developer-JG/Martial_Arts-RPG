from random import choice
from random import randint
import time

print("\nthe Martial Arts RPG game project\n")

po_count = 0
ag_count = 0
ad_count = 0

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

# 무술 인벤토리
def martial_arts_inventory(self):
    while True:
        ans = input("\n인벤토리를 선택하세요 [메인 무공 (q) /서브 무공 (w)]")
        print("나가려면 (enter)")
        if ans == "q" or ans == "w":
            martial_arts_inventory_print(self, ans)
        elif ans == "":
            break
        else:
            print("올바른 문자를 입력하세요")

# 아이템 프린트 2
def print_item_2(item):
    if item.use == 'atk':
        print("{0} : {1}\n{2} : {3}".format( \
            '이름', item.name, \
            '설명', item.damage)

# 아이템 프린트 1
def item_print_1(self, use, item, ans):
    while True:
        item_print_2(item[ans])
        ans = input("\n{0}을(를) 사용하시겟습니까? (y / n) : ".format(item[item].name))
        if ans == "y":
            if use == 're':

            item[item].count -= 1
            if item[item].count <= 0:
                del item[item]
            return self
        elif ans == "n":
            break
        else:
            print("올바른 문자를 입력하세요")

# 인벤토리 출력
def inventory(self):
    while True:
        print(f"{'인벤토리':=^25}")
        print("{0:^12}{1:^12}".format("Num", "Name"))
        if len(self.inven[item]) == 0:
            print("{0:^12}{1:^12}".format("없음", "없음"))
        for i in range(len(self.inven[item])):
            print("{0:^12}{1:^12}".format(i + 1, self.inven[item][i].name + "  x" + str(self.inven[item][i].count)))
        print(f"{'인벤토리':=^25}")
        ans = input("아이템의 정보를 보고 싶다면 해당 아이템의 번호를 입력하세요\n나가려면 (enter)\n:")
        ans = check(ans, 1, len(self.inven[item]))
        if type(ans) == type(0):
            print("\n{0:=^25}".format("Num" + str(ans) + " 정보"))
            ans -= 1
            item_print_1(self, ans, self.inven[item], ans)
        elif ans == "":
            break
        else:
            print("올바른 숫자를 입력하세요")

# 스텟
def level_up(self):
    print("\n" * 2)
    print("=" * 25)
    print("=" * 25)
    print("{0:=^25}".format(" 레벨 업 "))
    print("=" * 25)
    print("=" * 25)
    self.liv += 1
    print('Lv. ' + str(self.liv) + ' 로 레벨업을 하였습니다\n')
    self.exp = 0

    while True:
        print("{0:=^25}".format(" 스텟 "))
        print("1 힘 스텟 {0}\
            \n2 민첩 스텟 {1}\
            \n3 모험 스텟 {2}".format(po_count, ag_count, ad_count))

        num = input(":")
        if num == '1':
            if po_count == 50:
                continue
            print("{0:=^25}".format(" 힘 스텟 "))
            print("스텟 1당 공격력이 0.5% 증가합니다.")
            ans = input("y / n : ")
            if ans == 'y':
                print("공격력 0.5% 가 추가 됩니다")
                po_count += 1
                break
            elif ans == 'n':
                continue

        elif num == '2':
            if ag_count == 50:
                continue
            print("{0:=^25}".format(" 민첩 스텟 "))
            print("스텟 1당 크리티컬 확률이 0.5% 증가합니다.")
            ans = input("y / n : ")
            if ans == 'y':
                print("크리티컬 확률 0.5% 가 추가 됩니다")
                ag_count += 1
                break
            elif ans == 'n':
                continue

        elif num == '3':
            if ad_count == 50:
                continue
            print("{0:=^25}".format(" 모험 스텟 "))
            print("스텟 1당 체력이 5 증가합니다.")
            sel = input("y / n : ")
            if sel == 'y':
                self.health += 6
                print("체력이 6 추가 됩니다.")
                ad_count += 1
                break
            elif sel == 'n':
                continue
        else:
            print("올바른 문자를 입력하세요")
    else:
        pass

# 턴 체크
def turn_chack(self, plag):
    # 레벨업 체크
    level_up_count = 0

    if self.liv == 1:
        if self.exp >= 4:
            self.exp -= 4
            self.liv += 1
            level_up_count += 1
    elif self.liv == 2:
        if self.exp >= 400:
            self.exp -= 400
            self.liv += 1
    elif 3 <= self.liv <= 4:
        if self.exp >= 300:
            self.exp -= 300
            self.liv += 1
            level_up_count += 1
    elif 5 <= self.exp <= 10:
        if self.exp >= self.exp * 100:
            self.liv += 1
            level_up_count += 1
    elif 11 <= self.exp <= 20:
        if self.exp >= 1000 + (self.exp - 10) * 200:
            self.liv += 1
            level_up_count += 1
    elif 21 <= self.exp <= 30:
        if self.exp >= 3000 + (self.exp - 20) * 300:
            self.liv += 1
            level_up_count += 1
    elif 31 <= self.exp <= 40:
        if self.exp >= 6000 + (self.exp - 30) * 400:
            self.liv += 1
            level_up_count += 1
    elif 41 <= self.exp <= 50:
        if self.exp >= 10000 + (self.exp - 40) * 500:
            self.liv += 1
            level_up_count += 1
    elif 51 <= self.exp <= 60:
        if self.exp >= 15000 + (self.exp - 50) * 600:
            self.liv += 1
            level_up_count += 1
    elif 61 <= self.exp <= 70:
        if self.exp >= 21000 + (self.exp - 60) * 700:
            self.liv += 1
            level_up_count += 1
    elif 71 <= self.exp <= 80:
        if self.exp >= 28000 + (self.exp - 70) * 800:
            self.liv += 1
            level_up_count += 1
    elif 81 <= self.exp <= 90:
        if self.exp >= 36000 + (self.exp - 80) * 900:
            self.liv += 1
            level_up_count += 1
    elif 91 <= self.exp <= 100:
        if self.exp >= 45000 + (self.exp - 90) * 1000:
            self.liv += 1
            level_up_count += 1
    elif 101 <= self.exp:
        if self.exp >= 5500:
            self.liv += 1
            level_up_count += 1

    if level_up_count != 0:
        level_up(self)

    # 아레나
    if player_1.point >= 500:
        player_1.Arena == 'Arena no.1 하북팽가'
    if 500 < player_1.point >= 1000:
        player_1.Arena == 'Arena no.2 제갈세가'
    if 1000 < player_1.point >= 1500:
        player_1.Arena == 'Arena no.3 남궁세가'
    if 1500 < player_1.point >= 2000:
        player_1.Arena == 'Arena no.4 개방'
    if 2000 < player_1.point >= 2500:
        player_1.Arena == 'Arena no.5 형산파'
    if 3500 < player_1.point >= 3000:
        player_1.Arena == 'Arena no.6 점창파'
    if 3000 < player_1.point >= 3500:
        player_1.Arena == 'Arena no.7 아미파'
    if 3500 < player_1.point >= 4000:
        player_1.Arena == 'Arena no.8 무당파'
    if 4000 < player_1.point >= 4500:
        player_1.Arena == 'Arena no.9 무림맹'
    if 4500 < player_1.point >= 5500:
        player_1.Arena == 'Legendary Arena 소림사 (challenger)'
    if 5500 < player_1.point >= 6500:
        player_1.Arena == 'Legendary Arena 소림사 (master)'
    if 6500 < player_1.point:
        player_1.Arena == 'Legendary Arena 소림사 (champion)'

# 게임 종료
def game_over():
    print("\n게임을 종료하시겠습니까?")
    while True:
        end_ans = input("y / n : ")
        if end_ans == "y":
            print("\n게임을 종료합니다")

            print("gmae over")
            break
        if end_ans == "n":
            print("\n게임을 계속 진행합니다.")
            main()

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

        turn_chack(self, plag)  # 아레나, 스텟(레벨)

        player_1.showinfo()

        print("{0} : {1}/{2}/{3}".format( \
            '나의스텟 (힘, 민첩, 모험)', po_count, ag_count, ad_count))

        if plag == 0:
            print("\n도움을 원한다면 'h' 입력")

        ans = input("\n무엇을 하시겠습니까? : ")

        if ans == "q" or ans == "w" or ans == "e" or ans == "r" or ans == "t" or ans == "y":

        elif ans == "a":
            martial_arts_inventory(self)
        elif ans == "s":
            inventory(self)
            continue
        elif ans == "d":
            showshop(self)
            continue
        elif ans == "a":
            print("\n게임설명\n전투시작 : q,w,e,r,t,y\n무술 장착 및 해제 : a\n인벤토리 : s\n상점 : d\n도움말 : z\n게임종료 : p\
                    \n한국어를 웬만하면 누르지 마세요.(버그의 원인이 됩니다.)\n다 읽으셨다면 enter.")
            input()
        elif ans == "p":
            game_over()
        else:
            print("다시 입력해 주십시오")

        plag += 1

if __name__ == "__main__":
    main()