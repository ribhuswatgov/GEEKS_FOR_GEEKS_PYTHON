def posOfRightMostBit(m, n):
    xor = m^n
    pos = 1
    data = True
    while data is True:
        if (xor & (1<<(pos-1)))==0:
            pos+=1
            continue
        return pos

print(posOfRightMostBit(4, 52))