earn = input("Введите выручку фирмы: ")
cost = input("Введите издержки фирмы: ")
if earn.isdigit() and cost.isdigit():       # Проверям являются ли оба значения числами
    earn = int(earn)
    cost = int(cost)
    profit = earn - cost        # Здесь мы находим прибыль фирмы. Положительную, отрицательную или равную нулю.
    if profit > 0:      # В случае если фирма вышла в прибыль
        print(f"Наша фирма вышла в прибыль в {profit}, \n Рентабельность прибыли составила целых {earn / cost}")
        worker = input("Пожалуйста, укажите численность сотрудников фирмы")
        if worker.isdigit():        # Проверям является ли значение сотрудников фирмы числом
            print(f"Прибыль фирмы на одного сотрудника составляет: {profit / int(worker)}")
        else:
            print("Ошибка! Необходимо ввести число.")
    elif profit < 0:    # Если прибыль оказалась отрицательной
        print(f"Наша фирма отработала с убытком в {profit}")
    else:       # Если прибыль оказалась равной нулю
        print(f"Наша фирма вышла в {profit}, что тоже неплохо")
else:
    print("Ошибка! Необходимо ввести число.")