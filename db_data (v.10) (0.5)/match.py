from random import choice
from random import randint
import math

# 매치
def match(player_1):
    NPC_liv = player_1.Arena * 5
    NPC_stats = NPC_liv * 5

    NPC_po_count = math.floor(NPC_stats / 3)
    NPC_ag_count = math.floor(NPC_stats / 3)
    NPC_ad_count = math.floor(NPC_stats / 3)

    remainder = NPC_stats - NPC_po_count * 3

    if remainder == 1:
        NPC_po_count += 1
    elif remainder == 2:
        NPC_po_count += 1
        NPC_ad_count += 1

    for_count = randint(50, 100)

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
            var = randint(0, math.floor(NPC_po_count / 2))
            NPC_po_count -= var
            if var_2 == 1:
                NPC_ag_count += var
            elif var_2 == 2:
                NPC_ad_count += var
        elif var_1 == 2:
            var = randint(0, math.floor(NPC_ag_count / 2))
            NPC_ag_count -= var
            if var_2 == 1:
                NPC_ad_count += var
            elif var_2 == 2:
                NPC_po_count += var
        elif var_1 == 3:
            var = randint(0, math.floor(NPC_ad_count / 2))
            NPC_ad_count -= var
            if var_2 == 1:
                NPC_po_count += var
            elif var_2 == 2:
                NPC_ag_count += var

        if var_3 == 1:
            for_count -= 1

    # NPC 이름 설정
    if player_1.Arena == 1:
        npc_name = ["섬전신도 팽도엽", "진산도 팽대형", "오호단문도 팽대회", "웅풍도 팽대집", "복호도 팽철영"]
    elif player_1.Arena == 2:
        npc_name = ["제갈도", "제갈선", "제갈승", "제갈명", "제갈영기"]
    elif player_1.Arena == 3:
        npc_name = ["철검서생 남궁조", "기협 남궁추", "검패 남궁철", "낙성군자 남군도", "절옥검 남궁진"]
    elif player_1.Arena == 4:
        npc_name = ["탈혼주개 손등", "철심수사 모관", "광권 종호", "옥취개 송결", "혹랑 변혁"]
    elif player_1.Arena == 5:
        npc_name = ["수석장로 용성음", "냉홈검 고진", "조화신검 사견심", "비응검 사공표", "칠지신검 좌군풍"]
    elif player_1.Arena == 6:
        npc_name = ["신풍우사 장거릉", "점창일독 백리궁", "제이장로 흔신풍검 도군홍", "제사장로 독검취응 백리장손", "십방신검 사효심", "신응검협 조빙심"]
    elif player_1.Arena == 7:
        npc_name = ["흑미륵 원정", "결진사태", "홍두타 계명", "독나한 계조", "온미륵 계통"]
    elif player_1.Arena == 8:
        npc_name = ["대엽진인", "목엽진인", "선엽진인", "헌령", "현우", "현수"]
    elif player_1.Arena == 9:
        npc_name = ["취록자 허설", "천금공자 혁리의", "십방랑자 사효심", "신검무적 진산월", "산수재 이정문", "소신승", "창천신룡", "복호도", "옥랑검군"]
    elif player_1.Arena == 10:
        npc_name = ["정화", "정선", "정결", "정현", "정명"]
    elif player_1.Arena == 11:
        npc_name = ["대광", "대방", "대각", "대종", "대절", "대범", "대현", "대원"]
    elif player_1.Arena == 12:
        npc_name = ["범범대사", "굉요 대선사", "굉법", "굉지", "굉도", "굉수", "굉원"]

    NPC_name = choice(npc_name)

def change_2(player_1):
    if player_1.condition == 1:
        return '-'
    if player_1.condition == 2:
        return '기절'