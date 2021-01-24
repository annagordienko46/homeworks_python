proceeds = int(input("Введите выручку: "))
expens = int(input("Введите сумму расходов: "))
result_1 = proceeds - expens
profitability = result_1 / proceeds * 100
if proceeds > expens:
    print(f"Поздравляю, вы получили прибыль {result_1}")
    print(f"рентабельсть равна {profitability} %")
staff = int(input("Сколько сотрудников в компании? "))
profit_staf = result_1 / staff
print(f"Один сотрубдик приносит прибыль: {profit_staf}")

if proceeds < expens:
    print(f"У вас убыток {result_1}")


