def is_right_mountain(arr):
    L_cc = R_cc = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            if R_cc:
                return False
            L_cc += 1
        elif arr[i] > arr[i+1]:
            if not L_cc:
                return False
            R_cc += 1
        else:
            return False
    return bool(L_cc and R_cc)
 
*arr, = map(int, input('->').split())
print(is_right_mountain(arr))
