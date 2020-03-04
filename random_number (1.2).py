from random import randint
import math

Arena = 5

opponent_liv = Arena * 5
opponent_stats = opponent_liv * 5

while True:
    opponent_po_count = math.floor(opponent_stats / 3)
    opponent_ag_count = math.floor(opponent_stats / 3)
    opponent_ad_count = math.floor(opponent_stats / 3)

    remainder = opponent_stats - opponent_po_count * 3

    if remainder == 1:
        opponent_po_count += 1
    elif remainder == 2:
        opponent_po_count += 1
        opponent_ad_count += 1

    for_count = randint(50,100)

    while for_count > 0:
        var_1 = randint(1, 300)
        var_2 = randint(1, 200)
        var_3 = randint(1, 2)

        if var_1 % 3 == 0:
            var_1 = 3
        elif var_1 % 2 == 0:
            var_1 = 2
        else:
            var_1 = 1

        if var_2 % 2 == 0:
            var_2 = 2
        else:
            var_2 = 1

        if var_1 == 1:
            var = randint(0, math.floor(opponent_po_count / 2))
            opponent_po_count -= var
            if var_2 == 1:
                opponent_ag_count += var
            elif var_2 == 2:
                opponent_ad_count += var
        elif var_1 == 2:
            var = randint(0, math.floor(opponent_ag_count / 2))
            opponent_ag_count -= var
            if var_2 == 1:
                opponent_ad_count += var
            elif var_2 == 2:
                opponent_po_count += var
        elif var_1 == 3:
            var = randint(0, math.floor(opponent_ad_count / 2))
            opponent_ad_count -= var
            if var_2 == 1:
                opponent_po_count += var
            elif var_2 == 2:
                opponent_ag_count += var

        if var_3 == 1:
            for_count -= 1

    print("1 힘 스텟 {0}\
        \n2 민첩 스텟 {1}\
        \n3 모험 스텟 {2}".format(opponent_po_count, opponent_ag_count, opponent_ad_count))

    input()