def print_invoice(inv):
    print("\n==========================")
    print("    SMART STORE    ")
    print("===========================")
    print("شماره فاکتور:", inv["number"])
    for item in inv["items"]:
        print(item["name"], ":", item["qty"], "عدد *", money(item["unit_price"]), 
            "=", money(item["total"]), "تومان")








# meno

def show_menu():
    print("\n===== SMART STORE =====")
    print("1. ثبت کالا های جدید")
    print("2.نمایش فهرست کالا ها")
    print("3.جست وجوی کالا ")
    print("4.ثبت خرید مشتری")
    print("5.نمایش فاکتور خرید ")
    print("6.نمایش گزارش فروش ")
    print("7.خروج از برنامه")
    
while True:
        show_menu()
        choice = input("شماره گزینه را وارد کنید:")
        if choice == "7":
            print("خدانگهدار")
            break
        else:
          print("این بخش هنوز ساخته نشده است.")
          
          
        