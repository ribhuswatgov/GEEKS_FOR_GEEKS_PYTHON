def swapBits(n):
    even = n & 0xAAAAAAAA #0xAAAAAAAA = 0b10101010101010101010101010101010 getting value of even position
    even = even >>1
    
    odd = n & 0x55555555 #0x55555555 = 0b1010101010101010101010101010101 getting value of odd position
    odd = odd<<1
    
    return even | odd