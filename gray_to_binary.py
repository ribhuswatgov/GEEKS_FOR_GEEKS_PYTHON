def graytobinary(n):
    num = n
    
    while n!=0:
        n = n>>1
        num = num^(n)

    return num

graytobinary(15)