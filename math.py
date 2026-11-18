# import math


# def calculator():
#     print("ماشین‌حساب ساده")
#     print("1) جذر        2) توان        3) فاکتوریل")
#     print("4) سینوس      5) لگاریتم طبیعی")
#     print("6) کسینوس     7) تانژانت")
#     print("8) ceil       9) floor")
#     print("10) exp       11) log10")
#     print("12) قدر مطلق  13) باقیمانده (fmod)")
#     print("0) خروج")

#     while True:
#         choice = input("\nانتخاب: ")

#         if choice == "0":
#             break
#         elif choice == "1":
#             n = float(input("عدد: "))
#             if n < 0:
#                 print("جذر عدد منفی تعریف نشده")
#             else:
#                 print("نتیجه:", math.sqrt(n))
#         elif choice == "2":
#             a = float(input("پایه: "))
#             b = float(input("توان: "))
#             print("نتیجه:", math.pow(a, b))
#         elif choice == "3":
#             n = int(input("عدد صحیح: "))
#             if n < 0:
#                 print("فاکتوریل برای عدد منفی تعریف نشده")
#             else:
#                 print("نتیجه:", math.factorial(n))
#         elif choice == "4":
#             deg = float(input("زاویه (درجه): "))
#             print("نتیجه:", math.sin(math.radians(deg)))
#         elif choice == "5":
#             n = float(input("عدد: "))
#             if n <= 0:
#                 print("لگاریتم فقط برای عدد مثبت تعریف شده")
#             else:
#                 print("نتیجه:", math.log(n))
#         elif choice == "6":
#             deg = float(input("زاویه (درجه): "))
#             print("نتیجه:", math.cos(math.radians(deg)))
#         elif choice == "7":
#             deg = float(input("زاویه (درجه): "))
#             print("نتیجه:", math.tan(math.radians(deg)))
#         elif choice == "8":
#             n = float(input("عدد: "))
#             print("نتیجه:", math.ceil(n))
#         elif choice == "9":
#             n = float(input("عدد: "))
#             print("نتیجه:", math.floor(n))
#         elif choice == "10":
#             n = float(input("عدد: "))
#             print("نتیجه:", math.exp(n))
#         elif choice == "11":
#             n = float(input("عدد: "))
#             if n <= 0:
#                 print("لگاریتم فقط برای عدد مثبت تعریف شده")
#             else:
#                 print("نتیجه:", math.log10(n))
#         elif choice == "12":
#             n = float(input("عدد: "))
#             print("نتیجه:", math.fabs(n))
#         elif choice == "13":
#             x = float(input("x: "))
#             y = float(input("y: "))
#             if y == 0:
#                 print("y نمی‌تونه صفر باشه")
#             else:
#                 print("نتیجه:", math.fmod(x, y))
#         else:
#             print("گزینه نامعتبر")


# calculator()