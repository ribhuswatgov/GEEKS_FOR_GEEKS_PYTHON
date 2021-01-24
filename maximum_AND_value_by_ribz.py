def maximumANDvalue(arr):
    res = 0
    for bit in range(31, -1, -1):
        
        pattern = res | 1<<bit
        count = 0
        for index in range (0,len(arr)):
            if (pattern & arr[index]) == pattern:
                count+=1
            else:
                continue
            
        if count>=2:
            res = pattern # or we can write that   res = res | (1<<bit)
        else:
            continue
        
    return res

print(maximumANDvalue([8, 3, 13, 14, 17]))
