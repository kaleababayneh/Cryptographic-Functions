def extended_eculidean(a,b):
    placeholder = 1
    r = [a,b,placeholder]
    s = [1,0,placeholder]
    t = [0,1,placeholder]
    print("r","s","k")
    k = 2
    while(r[k-2] != 0):
        k = 2
        rc = r
        sc = s
        tc = t
       
        q = rc[k-2] // rc[k-1]
        r[k] = rc[k-2] % rc[k-1]
        s[k] = sc[k-2] - q * sc[k-1]
        t[k] = tc[k-2] - q * tc[k-1]
        k = k + 1
        k = k % 3
        
        print(r)
    
    return r[k-2]

     
extended_eculidean(12,5)