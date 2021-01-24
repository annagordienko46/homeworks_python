time = int(input("Введите время в секундах: "))
hours = time//3600
minuts = (time / 60) % 60
minuts_2 = int(minuts)#
seconds = time % 60
print(f"чч:{hours} мм:{minuts_2} сс:{seconds}")

