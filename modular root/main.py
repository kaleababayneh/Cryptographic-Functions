def modularSmallRoot(x,p):
    root = 0
    for i in range(1,p):
        if ((i * i) % p == x):
            root = i
    smallroot = root if root < p/2  else  p - root
    
    return smallroot


