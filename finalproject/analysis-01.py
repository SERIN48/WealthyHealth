#Program id : analysis-01

myname=""
myage=0
myheight=0
myweight=0
myblood_pressure=0
myblood_sugar=0
select1=0
high_blood_pressure = None
low_blood_pressure = None
diabete = None

high_blood_pressure = myblood_pressure > 140
low_blood_pressure = myblood_preesure < 90
diabete = myblood_sugar > 120


print("안녕하세요~ \nWealthy Health 입니다!!")
#select1 = int(input("정보입력을 시작하려면 1번, 프로그램을 종료하려면 2번을 입력해주세요."))

#if select1 == 1 :
#    print("정보입력을 시작합니다.")
#   anlaysis01()
    

#def analysis01() :
#    myname = input("성함을 입력해주세요 : ")
#    myage = int(input("나이를 입력해주세요 : ")
#    print("반가워요~")
#    print(myname," 님, 다음질문에 정확히 답변해주세요.")



myname = input("성함을 입력해주세요 : ")
myage = int(input("나이를 입력해주세요 : ")
            
print("반가워요~")
print(myname," 님, 다음질문에 정확히 답변해주세요.")
                
myheight = int(input("신장을 입력해주세요 : ")
myweight = int(input("체중을 입력해주세요 : ")
myblood_pressure = int(input("혈압수치를 입력해주세요 : ")
myblood_sugar = int(input("혈당수치를 입력해주세요 : ")
                    
