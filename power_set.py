ip = "abc"
#op = [[]]
op = [""]
for index in range(1, 2**(len(ip))):
    #op.append([])
    set_combo = ""
    
    for index2 in range(0, len(ip)):

        if (index & (1<<index2))!=0:
            #op[index].append(ip[index2])
            set_combo+= ip[index2]

    op.append(set_combo)
        
print(op)
        
