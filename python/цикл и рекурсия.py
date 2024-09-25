
# def buble_sort_iter(lst):
#     for j in range(len(lst) - 1, 0, -1):
#         print(lst)
#         print(f'Джей равен {j}')
#         i = 0
#         while i < j:
#             print(f'Итое равно {i}')
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#             i += 1

#     print(lst)

# if __name__ == '__main__':
#     lst = [3, 4, 5, 0, 1]
#     buble_sort_iter(lst)


def buble_sort_r(lst):
    def buble_sort(index):
        if index == 0:
            return
        i = 0
        while i < index:
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i += 1
        buble_sort(index - 1)

    buble_sort(len(lst) - 1)
    return lst


if __name__ == '__main__':
    lst = [3, 4, 5, 0, 1]
    print(buble_sort_r(lst))
