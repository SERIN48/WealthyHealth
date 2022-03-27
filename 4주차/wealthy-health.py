#Program id : wealthy-health

myname=""
myage=0
myheight=0
myweight=0
list_me=[]

myname = input("성함을 입력해주세요 : ")
print("안녕하세요~ ",myname, "님", "\nWealthy Health 입니다!!")



myblood_pressure=0
myblood_sugar=0
high_blood_pressure = None
low_blood_pressure = None
diabete = None

myblood_pressure = int(input("혈압수치를 입력해주세요 : ")
myblood_sugar = int(input("혈당수치를 입력해주세요 : ")

high_blood_pressure = myblood_pressure > 140
low_blood_pressure = myblood_preesure < 90
diabete = myblood_sugar > 120                    
                    



myheight = int(input("신장을 입력해주세요 : ")
myweight = int(input("체중을 입력해주세요 : ")                    
mybmi = myweight/(myheight*myheight)

               
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
        print("고혈압")
        me.append("고혈압")

    if low_blood_pressure:
        print("저혈압")
        me.append("저혈압")
               
    if diabete :
        print("당뇨병")
        me.append("당뇨병")

print(list_me)
               
if "저체중" in list_me :
    print("저체중은 다양한 원인이 있지만, 활동량보다 섭취량이 적거나, 과도한 활동, 흡수 불량, 정신적요인 등이 원인이 됩니다.")
    print("저체중 환자는 면역력이 약하고 \n어린이의 경우 성장이 지연될 수 있으며, \n여성의 경우 무월경 상태가 나타날 수 있습니다.")
    print("저체중이라고 해서 무조건적으로 식사량을 늘리는 것은 좋은 방법이 아닙니다.")
    print("1일 3회의 규칙적인 식사와 평소보다 500~1000칼로리를 증가시킨 고열량 식사를 해야합니다.")
    print("음주나 흡연은 영양소의 흡수를 방해하므로 최대한 삼가하고, 유제품을 섭취하는 것이 좋습니다.")
    print("또한, 고기나 생선, 계란 등과 같은 단백질 식품을 매끼에 섭취해야하며, \n비타민과 무기질 섭취를 위해 과일도 같이 섭취해야 합니다.")

if "과체중" in list_me :
    print("과체중은 비만과는 다르게 체중이 적정체중 이상임을 의미합니다.")
    print("보통 운동이나 생활하는 것보다 음식칼로리가 높은 것을 섭취하면 발생합니다.")
    print("평소 앉아만 있는 습관이나 과식하는 습관, 대사 장애, 알콜중독, 수면 부족 등의 원인이 있습니다.")
    print("이는 만병의 근원이 되어 고혈압이나 심근경색, 월경 이상, 심리적 이상증상 등\n각종 질병이 발생하게 되므로 초기에 관리해주셔야 합니다.")
    print("섬유질이 풍부한 음식으로 포만감이 들도록 하는 식단을 지키는 것이 중요합니다.")
    print("채소나 콩류, 과일, 조류 식품들에 섬유질이 많이 포함되어 있습니다.")
    print("식단 외에도 시간을 할애해 운동을 병행하는 것이 중요합니다.")

if "고혈압" in list_me :
    print("고혈압의 대부분은 원인이 명확하지 않은 경우가 대부분입니다.")
    print("여러가지 원인이 있지만 유전적인 요인이 가장 흔하고, 비만, 짜게 먹는 습관, 운동 부족 등의 원인이 있습니다.")
    print("고혈압의 환자들은 염분과 지방을 줄이고 양질의 단백질을 섭취하는 것이 중요하다.")
    print("평소 패스트푸드를 먹는 습관이 있다면 빠른 시일내에 고쳐야 한다.")
    print("다시마나 김, 미역, 땅콩 등이 고혈압 예방식품이므로 이 식품들과 함께 혈압에 좋은 양파나 생강, 검은콩등을 섭취해주어야 한다.")
    print("또한 표고버섯과 가지, 메밀, 인삼 등은 혈압 강하식품이므로 식단에 포함시키는 것이 좋습니다.")
    
if "저혈압" in list_me :
    print("저혈압의 원인에는 여러가지가 있는데,\n부갑상선 질환, 부신 기능 부전 등의 내분비 문제가 있으면 낮은 혈압이 발생할 수 있습니다.")
    print("또한, 열이나 구토, 소화기 질환등에 의한 탈수로 저혈압이 올 수 있으며, 식단에 영양소가 부족하여 저혈압이 생길 수도 있습니다.")
    print("물을 많이 마시는 것이 중요하며, 나트륨을 섭취하는 것이 도움이 됩니다.")
    print("또한 식단 외에도 의료용 압박스타킹을 이용하여 다리에 쏠려있는 혈액을 위로 보내 저혈압에 도움을 줄 수 있습니다.")
    print("저지방 단백질을 섭취하는 것이 좋으며\n생선이나 유제품을 통해 비타민을 섭취하고 암녹색 채소를 통해 엽산을 섭취하는 것이 좋습니다.")
    print("적당한 카페인은 혈관을 수축시켜 혈압을 높이므로 적당량 섭취하는 것도 하나의 방법입니다.")

if "당뇨병" in list_me :
    print("당뇨병은 인슐린의 생산량이 부족하여 생기는 병입니다.")
    print("과체중과 운동부족이 원인이 될 수도 있고, 유전적인 요인이 원인이 될 수도 있습니다.")
    print("당뇨병환자들은 정상체중을 유지하기 위한 적정열량을 섭취해야 합니다.")
    print("이는 사람에 따라 다를 수 있으므로 의사의 진단이 필요합니다.")
    print("또한, 혈당을 안정시키기 위해서 하루에 세끼를 항상 일정 시간에 먹어야하며 영양의 밸런스가 잘 맞아야 합니다.")
    print("운동은 인슐린 감도를 좋게 하므로 식단 외에도 적당한 생활 속 운동을 하는 습관을 들여야 합니다.")


print("확인할 식단을 선택해주세요.")
select = int(input("1.저체중용 식단\n2.과체중용 식단\n3.고혈압용 식단\n4.저혈압용 식단\n5.당뇨병용 식단")
             

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


if select ==1 :
    print("규칙적인 하루 세끼 식사와 중간중간 너무 자극적이지 않은 간식을 섭취해주세요.")
    sampleList1 = random.sample(list_lowweighttan, 1)
    sampleList2 = random.sample(list_lowweightdan, 2)
    sampleList3 = random.sample(list_lowweightvit, 1)
    sampleList4 = random.sample(list_lowweightsnack, 2)
    print(sampleList1)
    print(sampleList2)
    print(sampleList3)
    print(sampleList4)


if select == 2 :
    print("포만감을 주는 음식들과 열량이 낮은 음식들을 섭취해야합니다.")
    sampleList5 = random.sample(list_overweighttan, 1)
    sampleList6 = random.sample(list_overweightdan, 1)
    sampleList7 = random.sample(list_overweightfib, 1)
    print(sampleList5)
    print(sampleList6)
    print(sampleList7)             

if select == 3 :
    print("염분과 지방을 줄이고 양질의 단백질을 섭취해야 하며, 패스트푸트 섭취량을 줄이세요.")
    print("섭취 칼로리를 줄여 한달에 1~2kg을 감량한다는 생각으로 식사하는 것이 좋습니다.")
    sampleList8 = random.sample(list_highbptan, 1)
    sampleList9 = random.sample(list_highbpdan, 2)
    sampleList10 = random.sample(list_highbpgood, 1)
    print(sampleList8)
    print(sampleList9)
    print(sampleList10)             

if select == 4 :
    print("물을 많이 마시고, 적정량의 나트륨을 섭취하는 식단을 지켜야 합니다.")
    print("식사는 평소대로 하되, 조금의 식사를 여러번 나누어 하루에 5~6번 식사하는 것이 좋습니다.")
    print("특별히 저혈압에 좋은 음식들을 소개해 드리겠습니다.")
    sampleList11 = random.sample(list_lowpbgood, 2)
    print(sampleList11)
    print("위의 두 음식을 오전간식과 오후간식으로 나누어 드시기 바랍니다.")
             
if select == 5 :
    print("균형있는 식사를 하는 것이 중요하며, 지방이 많은 음식이나 양념이 진한 음식은 피하셔야 합니다.")
    sampleList12 = random.sample(list_diabetetan, 1)
    sampleList13 = random.sample(list_diabetedan, 1)
    sampleList14 = random.sample(list_diabetevit, 2)
    print(sampleList12)
    print(sampleList13)
    print(sampleList14)
                 
















