# Метод сортировки списка по возрастанию (применена сортировка "пузырьком"):
def sort_nums(lst):
    for i in range(0, len(lst) - 1):
        for j in range(0, len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


# Метод определения позиции элемента:
def index_num(lst, n):
    low = 0
    high = len(lst) - 1
    index = -1
    while (low <= high) and (index == -1):
        middle = (low + high) // 2
        if lst[middle] < n <= lst[middle + 1]:
            index = middle
        else:
            if lst[middle] > n:
                high = middle - 1
            else:
                low = middle + 1

    return index


try:
    nums_list = list(map(int, input("Введите числа через пробел: ").split()))
    if len(nums_list) >= 2:  # проверка наличия как минимум 2-х чисел в последовательности
        try:
            num = int(input("\nВведите число: "))

        except ValueError:  # исключаем ввод "не числа"
            print("Введено не число :(")

        else:
            sort_nums_list = sort_nums(nums_list)
            if sort_nums_list[0] < num <= sort_nums_list[-1]:  # проверка удовлетворения условий для поиска индекса
                print("\nОтсортированный по возрастанию список: ", nums_list)
                print("\nИндекс элемента, меньшего, чем введённое число =", index_num(sort_nums_list, num))

            else:
                print("\nЧисло должно быть больше первого элемента в списке\n"
                      "или равно последнему элементу, или меньше его :(")

    else:
        print("\nВведите хотя бы два числа :(")

except ValueError:
    print("Введены не числа :(")  # исключаем ввод "не чисел"
