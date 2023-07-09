# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
#
# store = {
#     '12345': [
#         {
#             'quantity': 27,
#             'price': 42
#         },
#     ],
#     '23456': [
#         {
#             'quantity': 22,
#             'price': 510
#         },
#         {
#             'quantity': 32,
#             'price': 520
#         },
#     ],
#     '34567': [
#         {
#             'quantity': 2,
#             'price': 1200
#         },
#         {
#             'quantity': 1,
#             'price': 1150
#         },
#     ],
#     '45678': [
#         {
#             'quantity': 50,
#             'price': 100
#         },
#         {
#             'quantity': 12,
#             'price': 95
#         },
#         {
#             'quantity': 43,
#             'price': 97
#         },
#     ],
# }
#
# for product_name, product_id in goods.items():
#     total_price = 0
#     total_quantity = 0
#     for item in store[product_id]:
#         price = item['quantity'] * item['price']
#         total_price += price
#         total_quantity += item['quantity']
#
#     print(f"""Produkt nomi: {product_name},
# Produkt idisi: {product_id},
# Umumiy qiymati: {total_quantity},
# Umimiy narxi: {total_price}
# """)

### Function

# def user_info(lastname, name, work):
#     print(f'Foydalanuvchini ismi: {lastname} {name}')
#     print(f'Foydalanuvchini ish joyi: {work}')
# lastname = 'Muhiddinov'
# name = 'Jaloliddin'
# work = 'Student'
# user_info('Qo'chqorov', 'Abdurahmon', 'Workingplace') # pozitsion argumentlar
# user_info('Abdullayev', 'Shoilhom', 'Office')
# user_info(name=name, lastname=lastname, work=work)
# user_info(lastname, work=work, name=name)  # nomli argumentlar

# def get_user_info(name, lastname, work=None):
#     print(f'Foydalanuvchini ismi: {name} {lastname}')
#
#     if work:
#         print(f'Foydalanuvchini ishi: {work}')
#
# get_user_info('Abdurahmon', "Qo'chqorov")

# def get_degree(a, b=2):
#     return a ** b

# result = get_degree(2, 4)
# get_degree(3)
# print(result)

# def get_speed(s=None, t=None, v=None):
#     result = 0
#     if s and v and t:
#         result = 'Siz 3ta ma\'lumot kiritdingiz'
#     elif s and v:
#         result = s / v
#     elif s and t:
#         result = s / t
#     elif v and t:
#         result = v * t
#     return result
#
# S = get_speed(t=8, v=60)
# t = get_speed(s=800, v=60)
# print(t)

### *args - soni cheklanmagan shart bo'lmagan pozitsion argumentlar
### **kwargs - soni cheklanmagan shart bo'lmagan nomli argumentlar

def make_pizza(hamir, cheese, *args, **kwargs):
    print(f"Sizning pitsangizni hamiri: {hamir}, pishloq turi: {cheese}")

    if args and kwargs:
        print(f"Qo'shimcha narsalar: {args}")
        print(kwargs)
    elif kwargs:
        pass

make_pizza('drojali', 'matsarella', 'zaytun', 'cheder', qoziqorin='shampinion', meat='kolbasa')
# make_pizza('drojali', 'matsarella')


