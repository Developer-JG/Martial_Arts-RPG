# 스텟
def level_up(player_1):
    print("\n" * 2)
    print(f"\n\n{'=' * 25}\n{'=' * 25}\n{'=' * 25}\n{' 레벨 업 :=^25'}{'=' * 25}\n{'=' * 25}\nLv. {str(player_1.liv)} 로 레벨업을 하였습니다")

    stats_point == 5

    while stats_point > 0:
        print(f"{' 스텟 ':=^25}")
        print(f"1 힘 스탯 {po_count}\n2 민첩 스탯 {ag_count}\n3 모험 스탯 {ad_count}\n")

        num = input(":")
        if num == '1':
            if po_count == 50:
                continue
            print(f"{' 힘 스텟 ':=^25}")
            print("스텟 1당 공격력이 1% 증가합니다.")
            ans = input("y / n : ")
            if ans == 'y':
                print("공격력 1% 가 추가 됩니다")
                po_count += 1
                stats_point -= 1
            elif ans == 'n':
                continue

        elif num == '2':
            if ag_count == 50:
                continue
            print(f"{' 민첩 스텟 ':=^25}")
            print("스텟 1당 크리티컬 확률이 1% 증가합니다.")
            ans = input("y / n : ")
            if ans == 'y':
                print("크리티컬 확률 1% 가 추가 됩니다.")
                ag_count += 1
                stats_point -= 1
            elif ans == 'n':
                continue

        elif num == '3':
            if ad_count == 50:
                continue
            print(f"{' 모험 스텟 ':=^25}")
            print("스텟 1당 체력이 5 증가합니다.")
            ans = input("y / n : ")
            if ans == 'y':
                print("체력이 5 추가 됩니다.")
                ad_count += 1
                stats_point -= 1
            elif ans == 'n':
                continue
        else:
            print("올바른 문자를 입력하세요")
            print("\n" * 38)
    else:
        pass