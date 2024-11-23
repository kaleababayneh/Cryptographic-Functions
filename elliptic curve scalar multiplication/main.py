
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

def add (first_point, second_point, a , field):

    first_point_x, first_point_y = first_point
    second_point_x, second_point_y = second_point

    if (first_point_x == second_point_x and first_point_y == second_point_y):
        numerator = 3 * first_point_x * first_point_x + a
        denominator = 2 * first_point_y
        numerator = modp(numerator, field)
        denominator = modp(denominator, field)
        inverse_denominator = inverse_mod(denominator, field)

        slope = inverse_denominator * numerator
        slope = modp(slope, field)
        
    else:
        numerator = second_point_y - first_point_y
        denominator = second_point_x - first_point_x
        numerator = modp(numerator, field)
        denominator = modp(denominator, field)
        inverse_denominator = inverse_mod(denominator, field)

        slope = inverse_denominator * numerator
        slope = modp(slope, field)


    x = (slope * slope) - first_point_x - second_point_x
    y = slope * (first_point_x - x) - first_point_y

    return [modp(x, field) , modp(y, field)]

def modp(n,p):
    return n % p


def scalar_mul(first_point, a ,n, field):
    Q = first_point
    R = 0
    while(n > 0):
        if (n%2 == 1):
            if ( R == 0):
                R = Q
            else:
                R = add(R,Q,a,field)
        Q = add(Q,Q,a,field)
        n = n // 2

    return R

print(scalar_mul([2339,2213], 497,7863, 9739))
 
