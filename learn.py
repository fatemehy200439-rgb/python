
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# #معرفی برنامه

# print("سلام! \n من دستیار هوشمند تو هستم.بیا وضعیت امروزت رو بررسی کنیم!🤖 ")

# #User data collection
# name = input("نامت چیست؟:")
# age = input("چند سالته؟:")
# grade =input("پایه تحصیلی ات چیست؟ :")
# study_hours = float(input("امروز چند ساعت مطالعه کردی؟:"))
# last_exam_score = float(input("نمره آخرین امتحانت چند بود؟:"))
# energy =int(input("میزان انرژی امروزت از ۱تا۱۰چنده؟:"))

# #Study time review
# if study_hours <= 1:
#     print("امروز مطالعه کمی داشتی😴 .بهتره زمان بیشتری به درس اختصاص بدی :")
# elif 1<=study_hours <=3:
#     print("مطالعه امروزت قابل قبول بوده است👍 :")
# elif study_hours >=3: 
#     print("عالیه🔥!امروز مطالعه خوبی داشتی.:")
 
#  #Last exam score  
# if last_exam_score <10:
#     print("نمره ات پایین بود💔!بهتر نقاط ضعفت رو پیدا کنی.")
# elif last_exam_score <15:
#     print("نمره ات متوسط با تمرین بیشتر میتونی بهترش کنی😕 !")
# elif last_exam_score <18:
#     print("عملکرد خوبی داشتی. ادامه بده🌟!")
# else:
#     print("عالی👏!عملکرد فوق العاده ای داشتی.")
     
# #Energy level
# if energy <3:
#      print("امروز انرژی کمی داری;بهتره کمی استراحت کنی😴 !")
     
# elif energy <7:
#     print("انرژیت مناسبه;میتونی روی تمرین هات کار کنی😊!")
# else:
#     print("انرژی فوق العاده ای داری!امروز فرصت خوبی برای پیشرفته🔋!")
    
# #study time and grade
# if study_hours <1 and last_exam_score <10:
#     print("امروز هم مطالعه ات کم بوده و هم نمره ات پایین بوده")
#     print("بهتره فردا زمان بیشتری برای مطالعه بزاری 📚")
# elif study_hours >3 and last_exam_score <10:
#     print("زیاد مطالعه کردی ,اما نمره ات وایین بوده 🤔 ")
#     print("بهتره روش مطالعه ات رو تغییر بدی🧠 ")
# elif study_hours >3 and last_exam_score <15:
#     print("مطالعه زیاد و نمره خوب👏 ")    
#     print("روش فعلیت نتیجه خوبی داشته,ادامه بده🌟")    
# else:
#     print("وضعیتت خوب و متعادله👍")  
#     print("با کمی تلاش بیشتر میتونی بهتر بشی🌱")
    
#     #Performance level
#     daily_score = (last_exam_score /20)*50 + (energy /10)*30 + min(study_hours / 5 ,1)*20
#     print("امتیاز امروزت📊 :", daily_score)
     
#     if daily_score >=80:
#         print("عملکرد فوق العاده ای داشتی 🏆") 
#     elif daily_score >=60:
#         print("عملکرد خوبی داشتی👍")
#     elif daily_score >=40:
#         print("عملکردت متوسط بود😊")
#     else:
#         print("فردا میتونی بهتر عمل کنی 🌱")            
    
#     #Proposed plan  
#     print("برنامه پیشنهادی فردا📚")
    
#     if study_hours <1:
#         print("فردا حداقل ۲ ساعت مطالعه کن.📖 ")
#     elif study_hours <=3:
#         print("فردا حدود ۳ ساعت مطالعه داشته باش 📖 ")
#     else:
#         print("فردا همین میزان مطالعه رو حفظ کن و استراحت کافی داشته باش.🧠")
    
#       #Final Report
#     print("================================")
#     print("گزارش نهایی دستیار هوشمند📋") 
#     print("================================")
    
#     print("نام👤", name)
#     print("سن🎂", age)  
#     print("پایه📚", grade)
#     print("ساعت مطالعه⏰", study_hours)
#     print("نمره امتحان📖", last_exam_score)
#     print("میزان انرژی🔋", energy)
#     print("امتیاز روزانه🏆", daily_score,"از100")
    
#     print("=================================")
#     print("گزارش امروزت اماده شد🤖")
#     print("ادامه بده و هر روز بهتر شو🚀")
#     print("=================================")
    
#     #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    
 #class_average   
    
# total = 0
# grade_counter = 0
# grades = [90,23,54,45,75,95,85,100,51,65]

# for grade in grades:
#     total += grade
#     grade_counter += 1
    
# avarage = total / grade_counter
# print(f'Class Avarage is {avarage}')

#...........................................#


# total = 0
# grade_counter = 0
# grades = [98,23,56,45,75,95,85,100,52,65]

# for grade in grades:
#     total += grade
#     grade_counter += 1
    
# avarage = total / grade_counter
# print(f'Class Avarage is {avarage}')

#.....................................#

#clacc_average_sentinel

# total = 0
# grade_counter = 0

# grade = int(input('Enter Your Number, -10 To End : '))

# while grade != -10:
#     total += grade
#     grade_counter += 1
#     grade = int(input('Enter Your Number, -10 To End : '))
    
# if grade_counter != 0:
#     avarage = total // grade_counter
#     print('-----------------------------')
#     print(f'Class Avarage Is {avarage}')
#     print('-----------------------------')
# else:
#     print('No Grade Were Entered')

#.....................................................#
