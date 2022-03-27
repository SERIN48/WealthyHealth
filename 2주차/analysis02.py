#Program id : analysis02


from analysis01 import myheight
from analysis01 import myweight
from analysis01 import mygender
from analysis01 import myblood_pressure
from analysis01 import myblood_sugar
from analysis01 import high_blood_pressure
from analysis01 import low_blood_pressure
from analysis01 import diabete


list_me=[]

#신장 & 체중
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


#혈압
if high_blood_pressure :
    print("고혈압입니다.")
    me.append("고혈압")
    
if low_blood_pressure :
    print("저혈압입니다.")
    me.append("저혈압")


#당뇨
if diabete :
    print("당뇨병입니다.")
    me.append("당뇨병")

