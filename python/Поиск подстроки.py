input_lst = input()
res = 0
string = ''
for symbol in input_lst:
    if symbol not in string:
        string += symbol
        res = max(res, len(string))
    else:
        cut = string.index(symbol)
        string = string[cut + 1:] + symbol
        print(string)
print(res)