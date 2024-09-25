def count_platforms(weight_list: list[int], limit: int) -> int:
    """ID 117581027"""
    """Задача решается по методу двух указателей."""
    left_counter = 0
    right_counter = len(weight_list) - 1
    count_platforms = 0
    weight_list = sorted(weight_list)
    while left_counter <= right_counter:
        if weight_list[left_counter] + weight_list[right_counter] <= limit:
            left_counter += 1
        count_platforms += 1
        right_counter -= 1
    return count_platforms


if __name__ == '__main__':
    weight_list = [int(x) for x in input().split()]
    limit = int(input())
    print(count_platforms(weight_list, limit))
