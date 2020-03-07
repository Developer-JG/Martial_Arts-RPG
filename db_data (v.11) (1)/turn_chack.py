# 턴 체크
def turn_chack(player_1):
    # 레벨업 체크
    level_up_count = 0

    if player_1.liv == 1:
        if player_1.exp >= 4:
            player_1.exp -= 4
            player_1.liv += 1
            level_up_count += 1
    elif player_1.liv == 2:
        if player_1.exp >= 400:
            player_1.exp -= 400
            player_1.liv += 1
    elif 3 <= player_1.liv <= 4:
        if player_1.exp >= 300:
            player_1.exp -= 300
            player_1.liv += 1
            level_up_count += 1
    elif 5 <= player_1.exp <= 10:
        if player_1.exp >= player_1.exp * 100:
            player_1.liv += 1
            level_up_count += 1
    elif 11 <= player_1.exp <= 20:
        if player_1.exp >= 1000 + (player_1.exp - 10) * 200:
            player_1.liv += 1
            level_up_count += 1
    elif 21 <= player_1.exp <= 30:
        if player_1.exp >= 3000 + (player_1.exp - 20) * 300:
            player_1.liv += 1
            level_up_count += 1
    elif 31 <= player_1.exp <= 40:
        if player_1.exp >= 6000 + (player_1.exp - 30) * 400:
            player_1.liv += 1
            level_up_count += 1
    elif 41 <= player_1.exp <= 50:
        if player_1.exp >= 10000 + (player_1.exp - 40) * 500:
            player_1.liv += 1
            level_up_count += 1
    elif 51 <= player_1.exp <= 60:
        if player_1.exp >= 15000 + (player_1.exp - 50) * 600:
            player_1.liv += 1
            level_up_count += 1
    elif 61 <= player_1.exp <= 70:
        if player_1.exp >= 21000 + (player_1.exp - 60) * 700:
            player_1.liv += 1
            level_up_count += 1
    elif 71 <= player_1.exp <= 80:
        if player_1.exp >= 28000 + (player_1.exp - 70) * 800:
            player_1.liv += 1
            level_up_count += 1
    elif 81 <= player_1.exp <= 90:
        if player_1.exp >= 36000 + (player_1.exp - 80) * 900:
            player_1.liv += 1
            level_up_count += 1
    elif 91 <= player_1.exp <= 100:
        if player_1.exp >= 45000 + (player_1.exp - 90) * 1000:
            player_1.liv += 1
            level_up_count += 1
    elif 101 <= player_1.exp:
        if player_1.exp >= 5500:
            player_1.liv += 1
            level_up_count += 1

    if level_up_count != 0:
        level_up(player_1)

    # 아레나
    if player_1.point <= 500:
        player_1.Arena == 1
    elif 500 < player_1.point <= 1000:
        player_1.Arena == 2
    elif 1000 < player_1.point <= 1500:
        player_1.Arena == 3
    elif 1500 < player_1_1.point <= 2000:
        player_1.Arena == 4
    elif 2000 < player_1.point <= 2500:
        player_1.Arena == 5
    elif 3500 < player_1.point <= 3000:
        player_1.Arena == 6
    elif 3000 < player_1.point <= 3500:
        player_1.Arena == 7
    elif 3500 < player_1.point <= 4000:
        player_1.Arena == 8
    elif 4000 < player_1.point <= 4500:
        player_1.Arena == 9
    elif 4500 < player_1.point <= 5500:
        player_1.Arena == 10
    elif 5500 < player_1.point <= 6500:
        player_1.Arena == 11
    elif 6500 < player_1.point:
        player_1.Arena == 12