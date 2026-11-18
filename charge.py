
# # get phone information and usage conditions

# charge =int(input("درصد شارژ گوشی را وارد کنید :"))
# outside_time = int(input("چند ساعت بیرون از خانه هستید؟"))
# Daily_usage =int(input("روزانه چند ساعد از گوشی استفاده می کنید؟"))
# Battery_health = input("وضعیت نگهداری شارژ باتری ؟(خوب ,متوسط,ضعیف)")
# charger = input("آیا به شارژر دسترسی دارید؟(بله/خیر)")
# powerbank = input("آیا پاوربانک دارید؟(بله/خیر)")
# print("اطلاعات شما ثبت شد.")
# # Estimate hourly battery consumption based on battery health
# if Battery_health == "ضعیف":
#     hourly_use = 15
# elif Battery_health == "متوسط":
#     hourly_use = 10
# elif Battery_health == "خوب":
#     hourly_use = 5
# print("مصرف تخمینی باتری در هر ساعت:", hourly_use)         
 
#  #calculate total estimated battery consumption
 
# total_consumption = hourly_use * outside_time
# print("میزان مصرف تخمینی کل باتری:", total_consumption, "درصد")
     
# # calculate remaining battery charge    
    
# remaining_charge = charge - total_consumption
# print("شارژ باقی مانده", remaining_charge, "درصد")
# if remaining_charge <= 10:
#     print("هشدار:شارژکافی نیست!")
#     print("حالت ذخیره انرژی را فعال کنید.")
# else:
#     print("شارژ گوشی کافی است.")
        
# # Display information and calculation results

# print("وضعیت شارژر", charger)
# print("وضعیت پاوربانک", powerbank)

# print("شارژ اولیه:", charge, "درصد")
# print("مصرف تخمینی:", total_consumption, "درصد")
# print("شارز باقی مانده:", remaining_charge, "درصد")

# # Check if the battery charge is sufficient

# if remaining_charge <= 10:
#     print("روشنایی صفحه را کاهش دهید.")
#     print("برنامه های پرمصرف راببندید.")
#     print("درصورت امکان گوشی را شارژ کنید.")
    
#     if charger == "بله" or powerbank == "بله":
#         print(" از شارژر یا پاوربانک استفاده کنید.")
#     else:
#         print("استفاده از گوشی را کاهش دهید.")        
    
     