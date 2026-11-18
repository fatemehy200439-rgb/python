
#Get the passengers trip information

distance = float(input("مسافت سفر را وارد کنید(km)."))
time = input("زمان سفر را مشخص کنید(روز/شب)")

base_fare = 20000
price_per_km = 8000


if distance <= 0:
    print("خطا!مسافت نامعتبر!")

else:
    if time == "شب":
      cost = base_fare + (distance * price_per_km)
      cost = cost * 1.20
      print("هزینه سفر شبانه اعمال شد.")
      print("هزینه نهایی سفر:", cost)
    
    elif time == "روز":
       cost = base_fare + (distance * price_per_km)
       cost = cost
       print("هزینه سفر روزانه اعمال شد.")
       print("هزینه نهایی سفر:", cost)
    
    else:
       print("زمان سفر نامعتبر است! روز یا شب را وارد کنید.")
    
            

