def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    return result + left[left_idx:] + right[right_idx:]

def merge_sort(array: list): # сортировка слиянием итерацией
    lsts = [[x] for x in array]
    print(lsts)
    while len(lsts) > 1:
        new_lsts = []
        for i in range(0, len(lsts) - 1, 2):
            print(lsts[i])
            new_lsts.append(merge(lsts[i], lsts[i + 1]))
        if len(lsts) % 2:
            new_lsts.append(lsts[-1])
        lsts = new_lsts
    return lsts[0]

if __name__ == '__main__':
    test_array = [5, 4, 9, 10, 8, 3, 11, 1, 7, 6, 2]
    print(merge_sort(test_array))