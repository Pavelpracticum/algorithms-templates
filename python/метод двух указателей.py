def find_two_indexes(data, expected_result):
    # В начале работы 
    # - левый указатель указывает на первый элемент списка (с индексом 0):
    left_pointer = 0
    # - правый указатель указывает на последний элемент списка. 
    # Индекс этого элемента на единицу меньше длины списка.
    right_pointer = len(data) - 1
    # Пока индекс левого указателя меньше индекса правого указателя.
    while left_pointer < right_pointer:
        # Считаем сумму двух элементов.
        if data[left_pointer] + data[right_pointer] == expected_result:
        # Если она совпадает с искомой...
        #...
            # ...возвращаем ответ:
            return expected_result
        # Если сумма больше искомой, то...
        elif data[left_pointer] + data[right_pointer] > expected_result:
            # ...надо уменьшить сумму: уменьшаем значение правого указателя.
            right_pointer -= 1
        # Все остальные варианты относятся к случаям, когда сумма меньше искомой.
        elif data[left_pointer] + data[right_pointer] < expected_result:
            # Сумму надо увеличить, для этого увеличиваем значение левого указателя.
            left_pointer += 1
    return


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_result = 10
    print(find_two_indexes(data, expected_result))