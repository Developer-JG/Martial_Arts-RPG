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