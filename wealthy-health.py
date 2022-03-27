#Program id : wealthy-health

import random

myname=""
myage=0
myheight=0
myweight=0
me=[]
myblood_pressure=0
myblood_sugar=0

myname = input("성함을 입력해주세요 : ")
print("안녕하세요~ ",myname, "님", "\nWealthy Health 입니다!!")


high_blood_pressure = None
low_blood_pressure = None
diabete = None

myblood_pressure = int(input("혈압수치를 입력해주세요 : "))
myblood_sugar = int(input("혈당수치를 입력해주세요 : "))

high_blood_pressure = myblood_pressure > 140
low_blood_pressure = myblood_pressure < 90
diabete = myblood_sugar > 120                    
                    
myheight = int(input("신장을 입력해주세요 : "))
myweight = int(input("체중을 입력해주세요 : "))
height = myheight/100
mybmi = myweight/(height*height)
if (mybmi <= 18.5) :
    print("저체중입니다.")
    me.append("저체중")

if (mybmi > 18.5 and mybmi <= 24.9) :
    print("정상체중입니다.")

if (mybmi > 24.9 and mybmi <=29.9) :
    print("과체중입니다.")
    me.append("과체중")

if (mybmi >29.9) :
    print("비만입니다.")
    me.append("비만")


if high_blood_pressure or low_blood_pressure or diabete :

    if high_blood_pressure:
        print("고혈압입니다.")
        me.append("고혈압")

    if low_blood_pressure:
        print("저혈압입니다.")
        me.append("저혈압")
               
    if diabete :
        print("당뇨병입니다.")
        me.append("당뇨병")

print(me)


while True :
    select1 = int(input("알아보고 싶은 정보의 번호를 입력해주세요:\n1.저제충\n2.과체중/비만\n3.고혈압\n4.저혈압\n5.당뇨병\n6.그만보기\n"))
    if (select1 == 1) :
        print("\n저체중은 다양한 원인이 있지만, 활동량보다 섭취량이 적거나, 과도한 활동, 흡수 불량, 정신적요인 등이 원인이 됩니다.")
        print("저체중 환자는 면역력이 약하고 \n어린이의 경우 성장이 지연될 수 있으며, \n여성의 경우 무월경 상태가 나타날 수 있습니다.")
        print("저체중이라고 해서 무조건적으로 식사량을 늘리는 것은 좋은 방법이 아닙니다.")
        print("1일 3회의 규칙적인 식사와 평소보다 500~1000칼로리를 증가시킨 고열량 식사를 해야합니다.")
        print("음주나 흡연은 영양소의 흡수를 방해하므로 최대한 삼가하고, 유제품을 섭취하는 것이 좋습니다.")
        print("또한, 고기나 생선, 계란 등과 같은 단백질 식품을 매끼에 섭취해야하며, \n비타민과 무기질 섭취를 위해 과일도 같이 섭취해야 합니다.\n")
        continue

    if (select1 == 2) :
        print("\n보통 운동이나 생활하는 것보다 음식칼로리가 높은 것을 섭취하면 발생합니다.")
        print("평소 앉아만 있는 습관이나 과식하는 습관, 대사 장애, 알콜중독, 수면 부족 등의 원인이 있습니다.")
        print("이는 만병의 근원이 되어 고혈압이나 심근경색, 월경 이상, 심리적 이상증상 등\n각종 질병이 발생하게 되므로 초기에 관리해주셔야 합니다.")
        print("섬유질이 풍부한 음식으로 포만감이 들도록 하는 식단을 지키는 것이 중요합니다.")
        print("채소나 콩류, 과일, 조류 식품들에 섬유질이 많이 포함되어 있습니다.")
        print("식단 외에도 시간을 할애해 운동을 병행하는 것이 중요합니다.\n")
        continue

    if (select1 == 3) :
        print("\n고혈압의 대부분은 원인이 명확하지 않은 경우가 대부분입니다.")
        print("여러가지 원인이 있지만 유전적인 요인이 가장 흔하고, 비만, 짜게 먹는 습관, 운동 부족 등의 원인이 있습니다.")
        print("고혈압의 환자들은 염분과 지방을 줄이고 양질의 단백질을 섭취하는 것이 중요하다.")
        print("평소 패스트푸드를 먹는 습관이 있다면 빠른 시일내에 고쳐야 한다.")
        print("다시마나 김, 미역, 땅콩 등이 고혈압 예방식품이므로 이 식품들과 함께 혈압에 좋은 양파나 생강, 검은콩등을 섭취해주어야 한다.")
        print("또한 표고버섯과 가지, 메밀, 인삼 등은 혈압 강하식품이므로 식단에 포함시키는 것이 좋습니다.\n")
        continue

    if (select1 == 4) :
        print("\n저혈압의 원인에는 여러가지가 있는데,\n부갑상선 질환, 부신 기능 부전 등의 내분비 문제가 있으면 낮은 혈압이 발생할 수 있습니다.")
        print("또한, 열이나 구토, 소화기 질환등에 의한 탈수로 저혈압이 올 수 있으며, 식단에 영양소가 부족하여 저혈압이 생길 수도 있습니다.")
        print("물을 많이 마시는 것이 중요하며, 나트륨을 섭취하는 것이 도움이 됩니다.")
        print("또한 식단 외에도 의료용 압박스타킹을 이용하여 다리에 쏠려있는 혈액을 위로 보내 저혈압에 도움을 줄 수 있습니다.")
        print("저지방 단백질을 섭취하는 것이 좋으며\n생선이나 유제품을 통해 비타민을 섭취하고 암녹색 채소를 통해 엽산을 섭취하는 것이 좋습니다.")
        print("적당한 카페인은 혈관을 수축시켜 혈압을 높이므로 적당량 섭취하는 것도 하나의 방법입니다.\n")
        continue

    if (select1 == 5) :
        print("\n당뇨병은 인슐린의 생산량이 부족하여 생기는 병입니다.")
        print("과체중과 운동부족이 원인이 될 수도 있고, 유전적인 요인이 원인이 될 수도 있습니다.")
        print("당뇨병환자들은 정상체중을 유지하기 위한 적정열량을 섭취해야 합니다.")
        print("이는 사람에 따라 다를 수 있으므로 의사의 진단이 필요합니다.")
        print("또한, 혈당을 안정시키기 위해서 하루에 세끼를 항상 일정 시간에 먹어야하며 영양의 밸런스가 잘 맞아야 합니다.")
        print("운동은 인슐린 감도를 좋게 하므로 식단 외에도 적당한 생활 속 운동을 하는 습관을 들여야 합니다.\n")
        continue

    if (select1 <=0 or select1>6) :
        print("\n잘못 선택하셨습니다. 다시 선택해주세요.\n")
        continue

    else :
        break
        

list_lowweighttan = ["흰쌀밥", "현미밥", "흑미밥"]
list_lowweightdan = ["고등어구이", "목살(150g)", "양념갈비", "계란말이", "계란후라이"]
list_lowweightvit = ["가지무침", "사과", "딸기", "감귤", "오이무침"]
list_lowweightsnack = ["케이크", "아이스크림","요구르트","푸딩"]

list_overweighttan = ["현미밥(1/2공기)", "흑미밥(1/2공기)", "고구마"]
list_overweightdan = ["훈제란", "닭가슴살", "닭가슴살 소세지", "삶은계란", "스테이크"]
list_overweightfib = ["샐러드믹스", "상추샐러드", "자몽", "토마토", "블루베리", "사과", "수박"]

list_highbptan = ["현미밥", "검은콩밥", "조밥"]
list_highbpdan = ["삶은계란", "두부구이", "가지구이", "표고버섯볶음"]
list_highbpgood = ["땅콩", "귤", "인삼차", "생강차"]

list_lowbpgood = ["다크초콜릿", "귤 2개", "로즈마리 차", "과일요거트", "커피 1잔"]

list_diabetetan = ["잡곡밥", "보리밥", "콩밥", "오곡밥"]
list_diabetedan = ["가지나물", "조기구이", "계란채소말이"]
list_diabetevit = ["사과반쪽", "아보카도샐러드", "토마토 1개", "배 반쪽"]


recipe = []

while True :
    print("확인할 식단을 선택해주세요.")
    select2 = int(input("1.저체중용 식단\n2.과체중용 식단\n3.고혈압용 식단\n4.저혈압용 식단\n5.당뇨병용 식단\n6.식단창 닫기"))
    if select2 ==1 :
        print("\n규칙적인 하루 세끼 식사와 중간중간 너무 자극적이지 않은 간식을 섭취해주세요.")
        sampleList1 = random.sample(list_lowweighttan, 1)
        sampleList2 = random.sample(list_lowweightdan, 2)
        sampleList3 = random.sample(list_lowweightvit, 1)
        sampleList4 = random.sample(list_lowweightsnack, 2)
        print(sampleList1)
        recipe.append(sampleList1)
        print(sampleList2)
        recipe.append(sampleList2)
        print(sampleList3)
        recipe.append(sampleList3)
        print(sampleList4)
        recipe.append(sampleList4)
        continue
    
    if select2 == 2 :
        print("\n포만감을 주는 음식들과 열량이 낮은 음식들을 섭취해야합니다.")
        sampleList5 = random.sample(list_overweighttan, 1)
        sampleList6 = random.sample(list_overweightdan, 1)
        sampleList7 = random.sample(list_overweightfib, 1)
        print(sampleList5)
        recipe.append(sampleList5)
        print(sampleList6)
        recipe.append(sampleList6)
        print(sampleList7)
        recipe.append(sampleList7)
        continue
        
    if select2 == 3 :
        print("\n염분과 지방을 줄이고 양질의 단백질을 섭취해야 하며, 패스트푸트 섭취량을 줄이세요.")
        print("섭취 칼로리를 줄여 한달에 1~2kg을 감량한다는 생각으로 식사하는 것이 좋습니다.")
        sampleList8 = random.sample(list_highbptan, 1)
        sampleList9 = random.sample(list_highbpdan, 2)
        sampleList10 = random.sample(list_highbpgood, 1)
        print(sampleList8)
        recipe.append(sampleList8)
        print(sampleList9)
        recipe.append(sampleList9)
        print(sampleList10)
        recipe.append(sampleList10)
        continue

    if select2 == 4 :
        print("\n물을 많이 마시고, 적정량의 나트륨을 섭취하는 식단을 지켜야 합니다.")
        print("식사는 평소대로 하되, 조금의 식사를 여러번 나누어 하루에 5~6번 식사하는 것이 좋습니다.")
        print("특별히 저혈압에 좋은 음식들을 소개해 드리겠습니다.")
        sampleList11 = random.sample(list_lowbpgood, 2)
        print(sampleList11)
        recipe.append(sampleList11)
        print("위의 두 음식을 오전간식과 오후간식으로 나누어 드시기 바랍니다.")
        continue
             
    if select2 == 5 :
        print("\n균형있는 식사를 하는 것이 중요하며, 지방이 많은 음식이나 양념이 진한 음식은 피하셔야 합니다.")
        sampleList12 = random.sample(list_diabetetan, 1)
        sampleList13 = random.sample(list_diabetedan, 1)
        sampleList14 = random.sample(list_diabetevit, 2)
        print(sampleList12)
        recipe.append(sampleList12)
        print(sampleList13)
        recipe.append(sampleList13)
        print(sampleList14)
        recipe.append(sampleList14)
        continue

    if (select2 <=0 or select2>6) :
        print("\n잘못 선택하셨습니다. 다시 선택해주세요.")

    else :
        break

print(recipe)
print("조리법을 확인해주세요.")
while True :
    print("\n조리법을 보고자 하는 요리의 번호를 선택해주세요.\n")
    select3 = int(input("1.고등어구이\n2.양념갈비\n3.계란말이\n4.가지무침\n5.오이무침\n6.상추샐러드\n7.두부구이\n8.가지구이\n9.표고버섯 볶음\n10.과일요거트\n11.가지나물\n12.조기구이\n13.계란채소말이\n14.아보카도샐러드\n15.그만보기\n"))
    
    if select3 == 1 :
        print("<고등어구이>\n")
        print("1.물기를 최대한 제거해주세요\n")
        print("2.밀가루나 부침가루를 묻혀 가루는 살살 털어내고 준비해주세요.\n")
        print("3.기름을 넉넉하게 두른 팬에서 센불로 1차 튀기듯 구워주세요.\n")
        print("4.두어번 뒤집는 정도로 끝내야 살이 망가지지 않고 좋아요.\n")
        print("5.가장자리가 노릇노릇할때 뒤집으면 됩니다.\n")
        continue
              
    if select3 == 2 :
        print("<양념갈비>\n")
        print("1.양념소스를 준비해주세요.\n")
        print("진간장 1컵, 설탕 반컵, 맛술 1컵, 물 1.5컵, 다진마늘 반컵, 생각 1숟가락, 다진 파 1컵, 참기름 1/3컵, 배즙 반컵, 후추조금을 넣고 섞어주세요.\n")
        print("2.양념장과 갈비를 섞고 재워주세요.\n")
        print("3.양념이 잘 배어진 갈비를 맛잇게 구워주세요.\n")
        continue
    
    if select3 == 3 :
        print("<계란말이>\n")
        print("1.계란 4개를 풀어주세요.\n")
        print("2.풀어진 계란에 당근이나 양파, 파 등을 잘게 썰어 기호에 맞게 넣어주세요.\n")
        print("3.후라이판에 올리고 익으면 가장자리부터 돌돌 말아주세요.\n")
        continue

    if select3 == 4 :
        print("<가지무침>\n")
        print("1.재료로는 가지 3개, 대파 1줄기, 통마늘 4톨이 필요합니다.\n")
        print("2.가지는 꼭지 부분을 손질하여 알뜰하게 끝까지 다 써주세요.\n")
        print("3.깨끗이 씻어 3등분해주시고 세로로 두어번 잘라 접시에 담아주세요.\n")
        print("4.썰어둔 가지는 비닐 랲이나 일회용 비닐봉지를 씌워 전자레인지에 2분씩 총 4번 돌려주세요.\n")
        print("5.마늘 4톨은 곱게 다지고 대파는 잘게 송송 썰어 준비해주세요.\n")
        print("6.가지는 전자레인지에서 꺼내 조금 식혀준 뒤 먹기좋게 찢어 준비해주세요.\n")
        print("7.찢어둔 가지에 진간장 1스푼, 참기름 1스품, 다진마늘 1스푼, 송송 썬 대파를 모두 넣고 통깨 2스푼을 잘 갈아서 깨소금을 만들어 잘 버무려주세요.\n")
        continue

    if select3 == 5 :
        print("<오이무침>\n")
        print("1.오이는 굵은 소금이나 천일염으로 박박 문질러서 깨끗이 씻어주세요.\n")
        print("2.오이를 먹기 좋은 크기로 썰고, 천일염 반큰술에 십분정도 절여주세요.\n")
        print("3.절인 오이를 물로 한번 행궈 물기를 빼주세요.\n")
        continue

    if select3 == 6 :
        print("<상추샐러드>\n")
        print("1.상추를 깨끗이 씻고 먹기좋게 잘라 주세요.\n")
        print("2.발사믹 소스를 두르고 잘 섞어주세요.\n")
        print("3.기호에 맞게 견과류(호두, 땅콩 등)나 소고기, 닭가슴살 등을 올려주세요.\n")
        continue

    if select3 == 7 :
        print("<두부구이>\n")
        print("1.키친타올을 깔고 두부를 올린뒤 소금을 뿌려서 잠시 재워주세요.\n")
        print("2.재워두었던 두부의 물기를 제거하고 기름을 두르고 구워주세요.\n")
        print("3.기회에 따라 홍고추를 같이 구워주면 매콤한 향이 나 더욱 맛있습니다.\n")
        continue

    if select3 == 8 :
        print("<가지구이>\n")
        print("1.앙념장을 먼저 만들게요.\n")
        print("부추와 대파를 잘게 썰고, 다진마늘과 고춧가루, 깨, 설탱을 넣고, 간장을 재료들이 살짝 잠길정도로만 넣고 섞어주세요.\n")
        print("참기름까지 넣고 섞으면 간장양념장이 완성됩니다. 매콤한 맛을 원하시면 청양고추를 조금 넣는 것도 좋아요.\n")
        print("2.가지를 오이소박이처럼 잘라주시고, 팬에 가지를 올려 구워주세요. 이때 식용유는 안넣으셔도 됩니다.\n")
        print("3.구운가지를 가지런히 놓고 그위에 양념장을 적절히 뿌려주세요.\n")
        continue

    if select3 == 9 :
        print("<표고버섯 볶음>\n")
        print("1.표고버섯의 밑동과 갓을 분리해주세요. 이번 요리는 갓 쪽을 사용할 거랍니다.\n")
        print("2.끓는 물(+소금 1t)에 표고버섯을 넣고 센불에서 2분 정도 데쳐주세요.\n")
        print("3.찬물에 여러 번 씻은 다음, 2개를 맞잡고 손으로 꼭 짜! 물기를 빼주면 된답니다.\n")
        print("4.그리고 0.5cm 두께로 도톰하게 썰어준 뒤, 여기에 소금 2/3t, 후추 약간을 넣고 조물조물 잘 섞어 밑간을 해주세요.\n")
        print("5.양파는 가늘게 채썰기, 대파는 어슷썰기, 홍고추는 쫑쫑쫑, 마늘 2알은 잘게 다져주세요.\n")
        print("6.예열된 프라이팬에 현미유를 두른 다음, 다진 마늘을 넣고 중불에서 30초 동안 볶아주세요. 양파가 투명하게 익을 때까지 볶아주면 된답니다.(대략 30초)\n")
        print("7.그리고 표고버섯, 굴소스, 집간장, 설탕을 넣고 5분 동안 볶아주면 된답니다.\n")
        print("8.마무리로 대파, 홍고추를 넣고 한 번 잘 저어준 다음 불을 꺼주세요.\n")
        print("9.마지막으로 부순 깨, 참기름을 넣고 뿌려주면 끝.\n")
        continue

    if select3 == 10 :
        print("<과일요거트>\n")
        print("1.시중에 파는 그릭요거트나 플레인 요거트 3스푼을 덜어주세요.\n")
        print("2.그 위에 원하는 과일을 먹기 좋은 사이즈로 잘라 올려주세요.\n")
        print("3.단맛을 원하시면 꿀을 조금 넣고 여러견과류를 잘게 부숴 올리고 섞어주시면 완성입니다.\n")
        continue

    if select3 == 11 :
        print("<가지나물>\n")
        print("1.가지를 씻어 꼭지를 딴 후, 적당한 크기로 잘라 찜기에 넣고 쪄주세요.\n")
        print("2.젓가락으로 찔러보았을때 가지가 잘 들어간다면 꺼내어 식혀주세요.\n")
        print("3.가지를 좀더먹기편하게 찢어서 꼭짜서물기를빼주세요.\n")
        print("4.다진마늘 ,국간장, 소금,들기름,갈은깨로 무쳐주세요.\n")
        print("5.간을보고 마지막에참기름을1티스푼넣고한번더무치면 가지나물완성입니다.\n")
        continue

    if select3 == 12 :
        print("<조기구이>\n")
        print("1.생선비늘을 벗기고 조기를 손질 한 후,깨끗한물에 씻어주고 소금으로 밑간만 살짝 해주세요.\n")
        print("2.후라이팬을 이용해 타지않게 앞뒤로 노릇하게 구워주세요.\n")
        print("3.구워진 생선은 그대로 먹어도 되고 유장처리를 해도 됩니다.\n")
        print("4.유장은 간장과 참기름만 섞어도 되는데 유장을 바르면 생선이 더 윤기있어 보인답니다.\n")
        continue

    if select3 == 13 :
        print("<계란채소말이>\n")
        print("1.계란을 풀어 주세요.\n")
        print("2.양파나 당근, 쪽파 등 원하는 채소를 최대한 잘게 잘라 계란 푼 물에 넣고 섞어주세요.\n")
        print("3.후라이팬에 올린 후 돌돌 말아 주면 완성입니다.\n")
        continue

    if select3 == 14 :
        print("<아보카도 샐러드>\n")
        print("1.여러 샐러드 채소를 섞거나 마트에 파는 샐러드 믹스를 준비해주세요.\n")
        print("2.아보카도를 잘라 반만 사용합니다.\n")
        print("3.기호에 따라 닭가슴살 조금이나 방울토마토 등의 과일을 올리면 완성입니다.\n")
        continue

    if select3 < 1 or select3 > 15 :
        print("번호를 잘못입력하셨습니다. 다시입력해주세요.")
        continue

    else :
        print("프로그램을 종료합니다.")
        print("Wealthy Health를 이용해주셔서 감사합니다.")
        break















