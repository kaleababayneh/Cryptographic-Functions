def add (first_point, second_point, a ,b, field):

    first_point_x, first_point_y = first_point
    second_point_x, second_point_y = second_point

    if (first_point_x == second_point_x and first_point_y == second_point_y):
        numerator = 3 * first_point_x * first_point_x + a
        denominator = 2 * first_point_y
        numerator = modp(numerator, field)
        denominator = modp(denominator, field)
        inverse_denominator = inverse(denominator, field)

        slope = inverse_denominator * numerator
        slope = modp(slope, field)
        
    else:
        slope = (second_point_y - first_point_y)/(second_point_x - first_point_y)


    x = (slope * slope) - first_point_x - second_point_x
    y = slope * (first_point_x - x) - first_point_y

    return modp(x, field) , modp(y, field)


def modp(n,p):
    return n % p

def inverse(n,p):
    return n;
    

