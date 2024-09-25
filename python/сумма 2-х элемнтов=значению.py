# def find_two_indexes(data, expected_sum):
#     # Ваше решение?
#     for index in range(len(data)):
#         for y in range(index+1, len(data)):
#             if data[index] + data[y] == expected_sum:
#                 return index, y
#     return


# if __name__ == '__main__':
#     data = [1, 2, 3, 4, 5, 6, 7, 11]
#     expected_sum = 10
#     print(find_two_indexes(data, expected_sum))




def find_two_indexes(data, expected_sum):
    # Для первого индекса и первого слагаемого.
    for first_index, first_value in enumerate(data):
        # Для второго индекса и второго слагаемого.
        for second_index, second_value in enumerate(data):
            # Если индексы равны, то есть это один и тот же элемент...
            if first_index == second_index:
                # ...переходим к следующему элементу.
                continue
            # Если сумма значений равна ожидаемому результату...
            if first_value + second_value == expected_sum:
                # ...вернуть индексы элементов.
                return first_index, second_index


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))
