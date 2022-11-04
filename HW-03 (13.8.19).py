# price2 = 990
# price1 = 1390
# price3 = 0
v_price = []
amount = 0
tickets_number = int(input("Количество билетов: "))
age = [int(input("Возраст посетителя: ")) for ticket in range(tickets_number)]
# print(age)
for visitor_age in age:
    if visitor_age < 18:
        price3 = 0
        v_price.append(price3)
    elif 25 > visitor_age >= 18:
        price2 = 990
        v_price.append(price2)
    else:
        price1 = 1390
        v_price.append(price1)
# print(v_price)
for price in v_price:
    amount += price
if tickets_number <= 3:
    print("Стоимость билетов: ", amount)
else:
    print("Полная стоимость билетов: ", amount)
    print("Ваша скидка: ", amount * 0.1)
    print("Стоимость билетов со скидкой: ", amount - (amount * 0.1))
