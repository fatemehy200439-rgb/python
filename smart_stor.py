# # Project: Smart Store Management System
# # ---------- Data ----------
# STORE_NAME = "NOKTEH SMART STORE"
# TAX_PERCENT = 9

# products = {}
# invoices = []


# # ---------- Helper functions ----------
# def money(amount):
#     return f"{int(amount):,}"


# def read_int(message, min_value=None):
#     while True:
#         text = input(message).strip()
#         try:
#             value = int(text)
#         except ValueError:
#             print("خطا: لطفاً یک عدد صحیح وارد کنید.")
#             continue
#         if min_value is not None and value < min_value:
#             print(f"خطا: عدد باید حداقل {min_value} باشد.")
#             continue
#         return value


# def calc_discount_percent(subtotal):
#     if subtotal >= 3_000_000:
#         return 15
#     elif subtotal >= 1_000_000:
#         return 10
#     elif subtotal >= 500_000:
#         return 5
#     return 0


# # ---------- Products ----------
# def add_product():
#     pid = read_int("شناسه کالا: ", 1)
#     if pid in products:
#         print("این شناسه قبلاً ثبت شده!")
#         return
#     name = input("نام کالا: ")
#     price = read_int("قیمت: ", 1)
#     stock = read_int("موجودی: ", 0)
#     products[pid] = {"name": name, "price": price, "stock": stock}
#     print("ثبت شد.")


# def show_products():
#     if not products:
#         print("کالایی نداریم.")
#         return
#     for pid, p in products.items():
#         print(pid, p["name"], money(p["price"]), p["stock"])


# def search_product():
#     query = input("شناسه یا نام کالا: ")
#     for pid, p in products.items():
#         if query == str(pid) or query == p["name"]:
#             print(pid, p["name"], money(p["price"]), p["stock"])
#             return
#     print("پیدا نشد.")


# # ---------- Invoice and purchase ----------
# def print_invoice(inv):
#     print("\n==============================")
#     print("      NOKTEH SMART STORE")
#     print("==============================")
#     print("شماره فاکتور:", inv["number"])
#     for item in inv["items"]:
#         print(item["name"], ":", item["qty"], "عدد *", money(item["unit_price"]),
#               "=", money(item["total"]), "تومان")
#     print("------------------------------")
#     print("مجموع خرید:", money(inv["subtotal"]), "تومان")
#     print("تخفیف:", inv["discount_percent"], "درصد")
#     print("مبلغ تخفیف:", money(inv["discount_amount"]), "تومان")
#     print("مبلغ پس از تخفیف:", money(inv["after_discount"]), "تومان")
#     print("مالیات:", money(inv["tax"]), "تومان")
#     print("------------------------------")
#     print("مبلغ نهایی:", money(inv["final"]), "تومان")
#     print("با تشکر از خرید شما!")


# def register_purchase():
#     cart = []

#     while True:
#         pid = read_int("شناسه کالا (برای پایان 0 بزنید): ", 0)
#         if pid == 0:
#             break
#         if pid not in products:
#             print("کالایی با این شناسه نیست.")
#             continue

#         p = products[pid]
#         qty = read_int("تعداد: ", 1)
#         if qty > p["stock"]:
#             print("موجودی کافی نیست.")
#             continue

#         p["stock"] = p["stock"] - qty
#         cart.append({
#             "name": p["name"],
#             "qty": qty,
#             "unit_price": p["price"],
#             "total": qty * p["price"],
#         })

#     if not cart:
#         print("خریدی ثبت نشد.")
#         return

#     subtotal = 0
#     for item in cart:
#         subtotal = subtotal + item["total"]

#     percent = calc_discount_percent(subtotal)
#     discount_amount = subtotal * percent // 100
#     after_discount = subtotal - discount_amount
#     tax = round(after_discount * TAX_PERCENT / 100)
#     final = after_discount + tax

#     inv = {
#         "number": 1001 + len(invoices),
#         "items": cart,
#         "subtotal": subtotal,
#         "discount_percent": percent,
#         "discount_amount": discount_amount,
#         "after_discount": after_discount,
#         "tax": tax,
#         "final": final,
#     }
#     invoices.append(inv)
#     print_invoice(inv)


# def show_invoice():
#     if not invoices:
#         print("هنوز فاکتوری صادر نشده.")
#         return
#     number = read_int("شماره فاکتور: ", 0)
#     for inv in invoices:
#         if inv["number"] == number:
#             print_invoice(inv)
#             return
#     print("فاکتوری با این شماره نیست.")


# # ---------- Sales report ----------
# def sales_report():
#     if not invoices:
#         print("هنوز هیچ فروشی ثبت نشده است")
#         return

#     total_qty = 0
#     total_subtotal = 0
#     total_discount = 0
#     total_tax = 0
#     total_final = 0
#     sold = {}

#     for inv in invoices:
#         total_subtotal = total_subtotal + inv["subtotal"]
#         total_discount = total_discount + inv["discount_amount"]
#         total_tax = total_tax + inv["tax"]
#         total_final = total_final + inv["final"]
#         for item in inv["items"]:
#             total_qty = total_qty + item["qty"]
#             name = item["name"]
#             sold[name] = sold.get(name, 0) + item["qty"]

#     best = max(sold, key=sold.get)
#     average = total_final / len(invoices)

#     print("\n================================")
#     print("          گزارش فروش")
#     print("================================")
#     print("تعداد فاکتورهای صادرشده:", len(invoices))
#     print("تعداد محصولات فروخته‌شده:", total_qty)
#     print("مجموع فروش قبل از تخفیف:", money(total_subtotal), "تومان")
#     print("مجموع تخفیف‌ها:", money(total_discount), "تومان")
#     print("مجموع مالیات:", money(total_tax), "تومان")
#     print("--------------------------------")
#     print("مجموع فروش نهایی:", money(total_final), "تومان")
#     print("--------------------------------")
#     print("پرفروش‌ترین محصول:", best)
#     print("میانگین مبلغ هر فاکتور:", money(average), "تومان")
#     print("================================")

#     answer = input("جزئیات همه فاکتورها نمایش داده شود؟ (y/n): ")
#     if answer == "y":
#         for inv in invoices:
#             print_invoice(inv)


# # ---------- Main menu ----------
# def show_menu():
#     print("\n===== SMART STORE =====")
#     print("1. ثبت کالای جدید")
#     print("2. نمایش فهرست کالاها")
#     print("3. جست‌وجوی کالا")
#     print("4. ثبت خرید مشتری")
#     print("5. نمایش فاکتور خرید")
#     print("6. نمایش گزارش فروش")
#     print("7. خروج از برنامه")


# while True:
#     show_menu()
#     choice = input("شماره گزینه را وارد کنید: ")
#     if choice == "1":
#         add_product()
#     elif choice == "2":
#         show_products()
#     elif choice == "3":
#         search_product()
#     elif choice == "4":
#         register_purchase()
#     elif choice == "5":
#         show_invoice()
#     elif choice == "6":
#         sales_report()
#     elif choice == "7":
#         print("خدانگهدار")
#         break
#     else:
#         print("گزینه نامعتبر است.")