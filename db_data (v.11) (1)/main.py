import time

from player import *
from inventory import *
from Martial_arts import *
from game_over import *
from level_up import *
from turn_chack import *
from match import *

print("\nthe Martial Arts RPG game project\n")

po_count = 0
ag_count = 0
ad_count = 0

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

        player_1 = Player(player_name, 1, 0, [], [], [], 0, 0, 0)
        plag = 0

    time.sleep(1.3)
    print('\n' * 2)
    print("정상적으로 로그인 되었습니다.")
    time.sleep(0.7)
    print("정보 불러오는 중...")
    time.sleep(0.7)
    print(f"환영합니다. {player_name}님")
    time.sleep(1)

    while True:

        print("\n" * 38)

        turn_chack(player_1)  # 아레나, 스텟(레벨)

        player_1.showinfo()

        print(f"나의스텟 (힘,민첩,모험) : {po_count}/{ag_count}/{ad_count}")

        if plag == 0:
            print("\n도움을 원한다면 'z' 입력")

        ans = input("\n무엇을 하시겠습니까? : ")

        if ans == "":
            match(player_1, po_count, ag_count, ad_count)
        elif ans == "q":
            martial_arts_inventory(player_1)
        elif ans == "w":
            inventory(player_1,'item')
            continue
        elif ans == "e":
            showshop(player_1)
            continue
        elif ans == "s":
            print("\n게임설명\n전투시작 : (enter)\n무술 장착 및 해제 : q\n인벤토리 : w\n상점 : e\n도움말 : s\n게임종료 : d\
                    \n한국어를 웬만하면 누르지 마세요.(버그의 원인이 됩니다.)\n다 읽으셨다면 enter.")
            input()
        elif ans == "d":
            game_over()
        else:
            print("다시 입력해 주십시오")

        plag += 1


if __name__ == "__main__":
    main()