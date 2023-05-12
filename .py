num_tickets = int(input("""При покупке от трёх билетов скидка 10%
Введите количество билетов: """))
total_cost = 0
num_free_tickets = 0
for i in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        num_free_tickets += 1
    elif age >= 18 and age < 25:
        total_cost += 990
    else:
        total_cost += 1390
if num_tickets > 3:
    total_cost *= 0.9
print("Сумма к оплате:", total_cost, "руб.")
