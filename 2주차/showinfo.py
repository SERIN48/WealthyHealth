#Program id : showinfo

from analysis02 import list_me

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
