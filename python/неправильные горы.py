#def is_right_mountain(arr):
 #   i_of_max = arr.index(max(arr))
  #  return i_of_max not in (0, len(arr)-1) and (all(R - L > 0 for (L, R) in zip(arr[:i_of_max], arr[1:i_of_max + 1]))
   #         and all(R - L < 0 for (L, R) in zip(arr[i_of_max:], arr[i_of_max + 1:])))
 
#*arr, = map(int, input('->').split())
#print(is_right_mountain(arr))


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
 
*arr, = map(int, input().split())
print(is_right_mountain(arr))
