tickets = int(input("Количество билетов: "))
price = 0

for t in range(tickets):
    age = int(input(f'Введите возраст {t+1} посетителя: '))

    if age >= 25:
        price += 1390

    elif 18 <= age < 25:
        price += 990

if tickets >= 3:
    price = int(price * 0.9)

print(f'К оплате: {str(price)} руб.')