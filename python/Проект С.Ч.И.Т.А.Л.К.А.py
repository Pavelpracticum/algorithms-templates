def win(n,k):
    out = 0
    lst = list(range(1, n + 1))
    print(lst)
    while len(lst) != 1:
        start = out % len(lst)
        print(start)
        out = (start + k - 1) % len(lst)
        print(out)
        print(lst[out])
        lst.remove(lst[out])
    return lst[0]


if __name__ == '__main__': 
    # n = int(input().strip())
    # k = int(input().strip())
    n = 5
    k = 2
    print(win(n,k))
# n = 5
# lst = list(range(1, n))
# print(lst)
