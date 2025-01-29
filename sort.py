def radix_sort(array):
    if not array:
        return array

    max_num = max(array)
    exp = 1  # Разряд
    while max_num // exp > 0:
        counting_sort_by_digit(array, exp)
        exp *= 10
    return array


def counting_sort_by_digit(array, exp):
    n = len(array)
    output = [0] * n
    count = [0] * 10  # 10 цифр (0-9)

    # Подсчитываем количество элементов по текущему разряду
    for num in array:
        index = (num // exp) % 10
        count[index] += 1

    # Обновляем индексы в массиве count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Заполняем отсортированный массив
    for i in range(n - 1, -1, -1):
        index = (array[i] // exp) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1

    # Копируем элементы обратно в исходный массив
    for i in range(n):
        array[i] = output[i]
