from inverse_mod import inverse_mod

print(inverse_mod(7,5))

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


print(add([8592, 2572],[2130, 2999],497,9739))
