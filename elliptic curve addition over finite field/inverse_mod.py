def extended_eculidean(a,b):
    reverse = False
    if (a < b):
        b,a = a,b
        reverse = True

    r0,r1,rk = a,b,1
    s0,s1,sk = 1,0,1
    t0,t1,tk = 0,1,1

    while(rk != 0):
        q = r0 // r1
        rk = r0 % r1
        sk = s0 - q * s1
        tk = t0 - q * t1

        r0,r1 = r1,rk
        s0,s1 = s1,sk
        t0,t1 = t1,tk

    if (reverse):
        return [r0, t0, s0]
    
    return [r0, s0, t0]

     
def inverse_mod(a,b):
    a1,b1,c1 = extended_eculidean(a,b)
    return b1

