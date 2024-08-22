def main():
    #int_list = list(map(int, input().strip().split()))
    input_lst = [int(x) for x in input().split()]
    search_value = int(input())
    
    index = 0
    try:
        index = input_lst.index(search_value, 0, len(input_lst) - 1)
    except ValueError:
        for item in input_lst:
            if len(set(input_lst)) == 1 and item > search_value:
                index = 0
            elif len(set(input_lst)) == 1:
                index = len(input_lst)
            elif item < search_value:
                index = input_lst.index(item) + 1

    print(index)


if __name__ == '__main__':
    main()
