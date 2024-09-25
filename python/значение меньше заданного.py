int_list = [int(x) for x in input().split()]
res = []
for i in range(len(int_list)):
    count = 0
    for j in range(len(int_list)):
        if int_list[j] < int_list[i]:
            count += 1
    res.append(count)

print(*res)
