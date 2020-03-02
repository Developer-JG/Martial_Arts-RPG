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
    def __init__(self, name, Arena, point, health, M_martial_arts_equipment, S_martial_arts_equipment, inven, condition, money, liv, exp):
        self.name = name
        self.Arena = Arena
        self.point = point
        self.health = health
        self.M_martial_arts_equipment = {"M_martial_arts_1": ["없음"], "M_martial_arts_2": ["없음"], "M_martial_arts_3": ["없음"], "M_martial_arts_4": ["없음"]}
        self.S_martial_arts_equipment = {"s_martial_arts_1": ["없음"], "s_martial_arts_2": ["없음"]}
        self.inven = {"main_martial_arts": [], "sub_martial_arts": [], "item": []}
        self.condition = condition
        self.money = money
        self.liv = liv
        self.exp = exp

    # 현재 상태 확인
    def showinfo(self):
        print(f"{'나의 상태':=^25}\n이름 : {self.name}\n레벨 : {self.liv}\n아레나 / 점수 : {self.Arena}{self.health}\n돈 : {self.money}")

    # 전투중 상태,무공 확인
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

    # 장착 무술 보기 1
    def m_martial_arts_equipment(self):
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

    # 장착 무술 보기 2
    def s_martial_arts_equipment(self):
        if len(self.S_martial_arts_equipment['S_martial_arts_1']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_2']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_2'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_2'][0]}")

# 무공 클래스
class martial_arts:
    def __init__(self,name,explanation,system,cool_time,count,use):
        self.name = name
        self.explanation = explanation
        self.system = system
        self.cool_time = cool_time
        self.count = count
        self.use = use

# 메인 무공
main_01 = martial_arts("용승권","1턴간 상대를 공격불능 상태로 만들고 5데미지를 준다.","패왕권법",2,25,'main')
main_02 = martial_arts("침무묵","2턴간 상대를 공격불능 상태로 만든다.","패왕권법",3,20,'main')
main_03 = martial_arts("금강불괴","내 데미지를 2턴간 50%으로 낮추고 상대방의 크리티컬 확률을 높인다.","패왕권법",3,15,'main')
main_04 = martial_arts("호장파풍","상대방에게 20 데미지를 주고 상대방을 1턴간 공격불능 상태로 만든다.","패왕권법",2,10,'main')
main_05 = martial_arts("패왕오의","4턴간 상대를 공격불능 상태로 만들고 턴당 10데미지를 준다.","패왕권법",5,5,'main')
main_06 = martial_arts("속박공","상대방에게 10에서 20데미지를 주고 스턴을 1턴간 건다.","반야술법",2,25,'main')
main_07 = martial_arts("섬무광탄","상대방을 5턴간 크리티컬 확률을 낮춘다. (20%)","반야술법",5,20,'main')
main_08 = martial_arts("시간역행","무공 쿨타임을 모두 없앤다.","반야술법",6,15,'main')
main_09 = martial_arts("호신강기","나와 상대방의 데미지를 2턴간 0으로 한다.","반야술법",6,10,'main')
main_10 = martial_arts("반야수인","나의 크리티컬확률을 1턴간 100%로 하고 상대방을 공격불능 상태로 만든다.","반야술법",2,5,'main')
main_11 = martial_arts("여래장","상대방에게 10데미지를 주고 2턴간 상대의 크리티컬확률이 매우 낮아진다. (5%)","여래장법",3,25,'main')
main_12 = martial_arts("오운천수","상대방에게 20데미지를 주고 5턴간 5데미지를 준다.","여래장법",6,20,'main')
main_13 = martial_arts("여강래회","2턴간 나의 크리티컬 확률이 올라간다. (80%)","여래장법",3,15,'main')
main_14 = martial_arts("폭발수인","1턴뒤 상대에게 20에서 40데미지를 준다.","여래장법",3,10,'main')
main_15 = martial_arts("여래수장","내 체력을 50 깎고 상대에게 40데미지를 준다.","여래장법",5,5,'main')
main_16 = martial_arts("태극의장","5턴간 상대방의 크리티컬 확률을 5%로 한다.","태극조화법",6,25,'main')
main_17 = martial_arts("의선의술","상대방의 체력을 80%로 회복시킨다.","태극조화법",5,20,'main')
main_18 = martial_arts("회복의술","나의 체력을 50% 회복시킨다.","태극조화법",5,15,'main')
main_19 = martial_arts("화룡강림","상대방을 2턴간 10데미지를 주고 50% 확률로 나의 데미지를 2턴간 무시한다.","태극조화법",3,10,'main')
main_20 = martial_arts("반탄공","공격의 80%를 반사하고 반사를 성공하였을때 4턴간 나의 데미지를 50%로 줄여준다.","태극조화법",7,5,'main')
main_21 = martial_arts("배위신","2턴간 상대의 크리티컬확률을 5%로 만들고 5턴간 3데미지를 준다.","당문비전",8,25,'main')
main_22 = martial_arts("독살포","3턴간 크리티컬확률을 5%로 만들고 2턴간 10데미지, 다음3턴간 5데미지를 준다.","당문비전",6,20,'main')
main_23 = martial_arts("하무정","2턴간 나의 크리티컬 확률을 100%로 만들고 상대방을 공격불능상태로 만든다.","당문비전",7,15,'main')
main_24 = martial_arts("만천화우","상대방에게 3턴간 15데미지를 준다.","당문비전",4,10,'main')
main_25 = martial_arts("후격지세","상대방에게 35, 20, 15, 5의 데미지를 순차적으로 입힌다.","당문비전",5,5,'main')

# 보조 무공
sub_01 = martial_arts("전격","50% 확률로 상대에게 15데미지를 주고 1턴간 공격불능상태로 만든다.",1,6,5,'sub')
sub_02 = martial_arts("뇌진법","50% 확률로 상대를 3턴간 공격불능 상태로 만든다.",1,6,5,'sub')
sub_03 = martial_arts("뇌전비술","50% 확률로 상대에게 15 ~ 30의 데미지를 주고 2턴간 공격불능 상태로 만든다.",1,6,5,'sub')
sub_04 = martial_arts("약골진","50% 확률로 상대 공격력을 2턴간 50%로 만든다.",2,6,5,'sub')
sub_05 = martial_arts("공복진","50% 확률로 상대 공격력을 2턴간 75%로 만들고 3턴간 크리티컬확률을 50%로 만든다.",2,6,5,'sub')
sub_06 = martial_arts("부동진","50% 확률로 나의 크리티컬 확률을 3턴간 80%로 만든다.",2,6,5,'sub')
sub_07 = martial_arts("기관진","50% 확률로 나의 공격력을 2턴간 125%로 만든다.",3,6,5,'sub')
sub_08 = martial_arts("회주복진","50% 확률로 나의 체력을 5턴간 10을 회복한다.",3,6,5,'sub')
sub_09 = martial_arts("회련진","50% 확률로 나의 체력을 40 회복한다.",3,6,5,'sub')
sub_10 = martial_arts("묘행진","50% 확률로 상대의 크리티컬 확률을 3턴간 50%로 만든다.",4,6,5,'sub')
sub_11 = martial_arts("풍속진","50% 확률로 상대의 크리티컬 확률을 2턴간 75% 로 만들고 나의 크리티컬 확률을 125% 로 만든다.",4,6,5,'sub')
sub_12 = martial_arts("멸살진","50% 확률로 상대의 크리티컬 확률을 2턴간 125%로 만들고 나의 공격력을 125%로 만든다.",4,6,5,'sub')

# 아이템 프린트 2
def item_print_2(item):
    if item.use == 'item':
        print("{0} : {1}\n{2} : {3}".format( \
            '이름', item.name, \
            '설명', item.damage)
    elif item.use == 'main':
        print("{0} : {1}\n{2} : {3}".format( \
            '이름', item.name, \
            '설명', item.damage)
    elif item.use == 'sub':
        print("{0} : {1}\n{2} : {3}".format( \
            '이름', item.name, \
            '설명', item.damage)

# 아이템 프린트 1
def item_print_1(self, ans, item):
    while True:
        item_print_2(item[ans])
        if item.use == item:
            ans_1 = input("\n{0}을(를) 사용하시겟습니까? (y / n) : ".format(item[ans].name))
            if ans_1 == "y":

                item[ans].count -= 1
                if item[ans].count <= 0:
                    del item[ans]
                return self
            elif ans_1 == "n":
                break
            else:
                print("올바른 문자를 입력하세요")
        elif item.use == item:
            ans_1 = input("\n{0} 무공을 착용 하시겟습니까? (y / n) : ".format(item[ans].name))
            if ans_1 == "y":

            elif ans_1 == 'n':
                break
            else:
                print("올바른 문자를 입력하세요")

# 인벤토리 출력
def inventory(self, ans):
    while True:
        ans_1 = change_1(ans)
        print("{0:=^25}".format(str(ans_1) + " 인벤토리"))
        print("{0:^12}{1:^12}".format("Num", "Name"))
        if len(self.inven[ans]) == 0:
            print("{0:^12}{1:^12}".format("없음", "없음"))
        if ans == 'main' or ans == 'sub':
            for i in range(len(self.inven[ans])):
                print("{0:^12}{1:^12}".format(i + 1, self.inven[ans][i].name))
        else:
            for i in range(len(self.inven[ans])):
                print("{0:^12}{1:^12}".format(i + 1, self.inven[ans][i].name + "  x" + str(self.inven[ans][i].count)))
        if ans == 'main' or ans == 'sub':
            ans_2 = input("\n아이템의 정보를 보고 싶다면 해당 아이템의 번호를 입력하세요\n나가려면 (enter)\n:")
        else:
            ans_2 = input("\n해당 무공의 정보를 보고 싶다면 해당 무공의 번호를 입력하세요\n나가려면 (enter)\n:")
        ans_2 = check(ans_2, 1, len(self.inven[ans]))
        if type(ans_2) == type(0):
            if ans == 'item':
                print("\n{0:=^25}".format("Num" + str(ans_2) + " 정보"))
                item_print_1(self, use, item)
            else:
                print("\n{0:=^25}".format(item.name + " 정보"))
            ans_2 -= 1
            item_print_1(self, use, item)
        elif ans_2 == "":
            break
        else:
            print("올바른 숫자를 입력하세요")

# 무술 인벤토리 프린트
def martial_arts_inventory_print(self, ans):
    if ans == 'q':
        print(f"{'장착중인 메인 무공':=^25}")
        m_martial_arts_equipment(self)
        inventory(self, main)
    elif ans == 'w':
        print(f"{'장착중인 서브 무공':=^25}")
        s_martial_arts_equipment(self)
        inventory(self, sub)


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

# 바꾸기
def change_1(ans):
    if ans == 1:
        return '아이템'
    elif ans == 2:
        return '메인 무공'
    elif ans == 3:
        return "보조 무공"

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
            inventory(self, item)
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