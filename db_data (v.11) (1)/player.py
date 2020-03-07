# 플레이어 클래스
class Player:
    def __init__(self, name, Arena, point, M_martial_arts_equipment, S_martial_arts_equipment, inven, money, liv, exp):
        self.name = name
        self.Arena = Arena
        self.point = point
        self.M_martial_arts_equipment = {"M_martial_arts_1": ["없음"], "M_martial_arts_2": ["없음"],
                                         "M_martial_arts_3": ["없음"], "M_martial_arts_4": ["없음"]}
        self.S_martial_arts_equipment = {"s_martial_arts_1": ["없음"], "s_martial_arts_2": ["없음"]}
        self.inven = {"main": [], "sub": [], "item": []}
        self.money = money
        self.liv = liv
        self.exp = exp

    # 현재 상태 확인
    def showinfo(self):
        player_arena = change(self.Arena)
        print(f"{'나의 상태':=^25}\n이름 : {self.name}\n레벨 : {self.liv}\n아레나 : {player_arena}\n점수 : {self.point}\n돈 : {self.money}")

    # 장착 무술 보기 1
    def martial_arts_equipment(self):
        if len(self.M_martial_arts_equipment['M_martial_arts_1']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_2']) == 2:
            print(f"2.{self.M_martial_arts_equipment['M_martial_arts_2'][1].name}")
        else:
            print(f"2.{self.M_martial_arts_equipment['M_martial_arts_2'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_3']) == 2:
            print(f"3.{self.M_martial_arts_equipment['M_martial_arts_3'][1].name}")
        else:
            print(f"3.{self.M_martial_arts_equipment['M_martial_arts_3'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_4']) == 2:
            print(f"4.{self.M_martial_arts_equipment['M_martial_arts_4'][1].name}")
        else:
            print(f"4.{self.M_martial_arts_equipment['M_martial_arts_4'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_1']) == 2:
            print(f"5.{self.S_martial_arts_equipment['S_martial_arts_1'][1].name}")
        else:
            print(f"5.{self.S_martial_arts_equipment['S_martial_arts_1'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_2']) == 2:
            print(f"6.{self.S_martial_arts_equipment['S_martial_arts_2'][1].name}")
        else:
            print(f"6.{self.S_martial_arts_equipment['S_martial_arts_2'][0]}")

    # 장착 무술 보기 2
    def m_martial_arts_equipment(self):
        if len(self.M_martial_arts_equipment['M_martial_arts_1']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_2']) == 2:
            print(f"2.{self.M_martial_arts_equipment['M_martial_arts_2'][1].name}")
        else:
            print(f"2.{self.M_martial_arts_equipment['M_martial_arts_2'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_3']) == 2:
            print(f"3.{self.M_martial_arts_equipment['M_martial_arts_3'][1].name}")
        else:
            print(f"3.{self.M_martial_arts_equipment['M_martial_arts_3'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_4']) == 2:
            print(f"4.{self.M_martial_arts_equipment['M_martial_arts_4'][1].name}")
        else:
            print(f"4.{self.M_martial_arts_equipment['M_martial_arts_4'][0]}")

    # 장착 무술 보기 3
    def s_martial_arts_equipment(self):
        if len(self.S_martial_arts_equipment['S_martial_arts_1']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_2']) == 2:
            print(f"2.{self.S_martial_arts_equipment['S_martial_arts_2'][1].name}")
        else:
            print(f"2.{self.S_martial_arts_equipment['S_martial_arts_2'][0]}")

# 바꾸기
def change(point):
    if point == 1:
        return 'Arena no.1 하북팽가'
    elif point == 2:
        return 'Arena no.2 제갈세가'
    elif point == 3:
        return 'Arena no.3 남궁세가'
    elif point == 4:
        return 'Arena no.4 개방'
    elif point == 5:
        return 'Arena no.5 형산파'
    elif point == 6:
        return 'Arena no.6 점창파'
    elif point == 7:
        return 'Arena no.7 아미파'
    elif point == 8:
        return 'Arena no.8 무당파'
    elif point == 9:
        return 'Arena no.9 무림맹'
    elif point == 10:
        return 'Legendary Arena 소림사 (challenger)'
    elif point == 11:
        return 'Legendary Arena 소림사 (master)'
    elif point == 12:
        return 'Legendary Arena 소림사 (champion)'