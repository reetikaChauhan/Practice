s = input()
count =0
logos = {}
if len(s) >= 3:
    for i in range(len(s)):
        if s[i] in logos.keys():
            pass
        else:
            count=1
            for j in range(i+1,len(s)):
                if s[i] == s[j] :
                    count=count+1 
        logos[s[i]] = count      
sort_orders = dict(sorted(logos.items(), key=lambda x: x[1], reverse=True)) 
occ = list(int(num) for num in sort_orders.values()) 
c=0 
for _ in occ:
    if( _ == occ[0] ):
        pass     
    else:
        for i in sort_orders:
            print(i,sort_orders[i])
            c = c+1
            if c >=3:
                break
        break
else:
    for m in sorted(logos):
        print(m,logos[m])
        c = c+1
        if(c>=3):
            break

            


    

        
    



