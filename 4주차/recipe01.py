#Program id : recipe01

import random
from analysis02 import list_me

list_lowweighttan = ["흰쌀밥", "현미밥", "흑미밥"]
list_lowweightdan = ["고등어구이(1마리)", "목살(150g)", "양념갈비(150g)", "계란말이", "계란후라이(2개)","계란장"]
list_lowweightvit = ["가지무침", "사과", "딸기", "감귤", "오이무침"]
list_lowweightsnack = ["케이크", "아이스크림","요구르트","푸딩"]

list_overweighttan = ["현미밥(1/2공기)", "흑미밥(1/2공기)", "고구마"]
list_overweightdan = ["훈제란", "닭가슴살", "닭가슴살 소세지", "삶은계란", "스테이크(70g)"]
list_overweightfib = ["샐러드믹스", "상추샐러드", "자몽", "토마토", "블루베리", "사과", "수박"]

list_highbptan = ["현미밥", "검은콩밥", "조밥"]
list_highbpdan = ["생선", "삶은계란", "두부조림", "가지구이", "표고버섯 볶음"]
list_highbpgood = ["땅콩", "귤", "인삼차", "생강차"]

list_lowbpgood = ["다크초콜릿", "귤 2개", "로즈마리 차", "과일요거트", "커피 1잔"]

list_diabetetan = ["잡곡밥", "보리밥", "콩밥", "오곡밥"]
list_diabetedan = ["갈치조림", "가지나물", "조기구이", "계란채소말이"]
list_diabetevit = ["사과반쪽", "아보카도샐러드", "토마토 1개", "배 반쪽"]



if "저체중" in list_me :
    print("규칙적인 하루 세끼 식사와 중간중간 너무 자극적이지 않은 간식을 섭취해주세요.")
    sampleList1 = random.sample(list_lowweighttan, 1)
    sampleList2 = random.sample(list_lowweightdan, 2)
    sampleList3 = random.sample(list_lowweightvit, 1)
    sampleList4 = random.sample(list_lowweightsnack, 2)
    print(sampleList1)
    print(sampleList2)
    print(sampleList3)
    print(sampleList4)

if "과체중" in list_me :
    print("포만감을 주는 음식들과 열량이 낮은 음식들을 섭취해야합니다.")
    sampleList5 = random.sample(list_overweighttan, 1)
    sampleList6 = random.sample(list_overweightdan, 1)
    sampleList7 = random.sample(list_overweightfib, 1)
    print(sampleList5)
    print(sampleList6)
    print(sampleList7)
    

if "고혈압" in list_me :
    print("염분과 지방을 줄이고 양질의 단백질을 섭취해야 하며, 패스트푸트 섭취량을 줄이세요.")
    print("섭취 칼로리를 줄여 한달에 1~2kg을 감량한다는 생각으로 식사하는 것이 좋습니다.")
    sampleList8 = random.sample(list_highbptan, 1)
    sampleList9 = random.sample(list_highbpdan, 2)
    sampleList10 = random.sample(list_highbpgood, 1)
    print(sampleList8)
    print(sampleList9)
    print(sampleList10)

if "저혈압" in list_me :
    print("물을 많이 마시고, 적정량의 나트륨을 섭취하는 식단을 지켜야 합니다.")
    print("식사는 평소대로 하되, 조금의 식사를 여러번 나누어 하루에 5~6번 식사하는 것이 좋습니다.")
    print("특별히 저혈압에 좋은 음식들을 소개해 드리겠습니다.")
    sampleList11 = random.sample(list_lowpbgood, 2)
    print(sampleList11)
    print("위의 두 음식을 오전간식과 오후간식으로 나누어 드시기 바랍니다.")

if "당뇨병" in list_me :
    print("균형있는 식사를 하는 것이 중요하며, 지방이 많은 음식이나 양념이 진한 음식은 피하셔야 합니다.")
    sampleList12 = random.sample(list_diabetetan, 1)
    sampleList13 = random.sample(list_diabetedan, 1)
    sampleList14 = random.sample(list_diabetevit, 2)
    print(sampleList12)
    print(sampleList13)
    print(sampleList14)
    
    
    
