def main():
    n = int(input())
    #n = input().split()
    #int_list = list(map(int, input().split()))
    int_list = [int(x) for x in input().split()]
    print(int_list)
    #int_list = sorted(input().split() for _ in range(n))
    new_list = []
    new_list_1 = []
    for index, value in enumerate(int_list):
        if value not in new_list:
            new_list.insert(int_list[index], value)
            print(int_list[index])
        elif value in new_list:
            new_list_1.append('_')
    list.extend(new_list, new_list_1)
    print(*new_list)


if __name__ == '__main__':
    main()
