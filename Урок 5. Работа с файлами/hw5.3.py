"""

Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

"""
with open("Список сотрудников.txt", "r+") as file:
    summ = 0
    surname = []

    # Сделаем список с сотрудниками и их окладами
    my_list = file.read().splitlines()
    worker = len(my_list)
    print("Список наших сотрудников:", my_list, "\n")

    for item in my_list:
        user_list = item.split()
        summ += int(user_list[1])
        if int(user_list[1]) < 20000:
            surname.append(user_list[0])

    print("Сотрудники с окладом менее 20 тыс.", surname, )
    print("Количество сотрудников:", worker)
    print("Средняя величина дохода сотрудников:", summ / worker)
