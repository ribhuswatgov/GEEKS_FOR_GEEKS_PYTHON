'''
Given two numbers M and N. The task is to find the position of rightmost different bit in binary representation of numbers.

Input Format:
The input line contains T, denoting the number of testcases. Each testcase follows. First line of each testcase contains two space separated integers M and N.

Output Format:
For each testcase in new line, print the position of rightmost different bit in binary representation of numbers. If both M and N are same then print -1 in this case.

User Task:
The task is to complete the function posOfRightMostDiffBit() which takes two arguments m and n and returns the position of first different bits in m and n.

Constraints:
1 <= T <= 100
1 <= M <= 103
1 <= N <= 103

Example:
Input:
2
11 9
52 4

Output:
2
5

Explanation:
Tescase 1: Binary representaion of the given numbers are: 1011 and 1001, 2nd bit from right is different.
'''

def posOfRightMostDiffBit(m,n):
    data = True
    pos = 1
    if m == n:
        return -1
        
    xor = m^n
    while data is True:
        if xor & (1<<pos-1) == 0:
            pos+=1
            continue
        else:
            data = False
            return pos
            
print(posOfRightMostDiffBit(4,5))