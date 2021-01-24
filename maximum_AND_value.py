def checkbit(pattern, arr):
    count = 0
    for index in range(0, len(arr)):
        flag = bin(arr[index])
        dec_to_bin = bin(pattern & arr[index])
        if (pattern & arr[index]) == pattern:
            count+=1
    
    return count

def maxAND(arr):
    res = 0

    for bit in range(5, -1, -1):
        pattern_in_binary = bin(res | (1<<bit))
        count = checkbit(res | (1<<bit), arr)

        if count>=2:
            res |= (1<<bit)
            result = bin(res)

    return res

print(maxAND([4,8,10,11,12,14]))
