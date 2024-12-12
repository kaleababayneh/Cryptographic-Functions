def modularSmallRoot(x,p):
    root = 0
    for i in range(1,p):
        if ((i * i) % p == x):
            root = i
    smallroot = root if root < p/2  else  p - root
    
    return smallroot

def modularBigRoot(x,p):
    root = 0
    for i in range(1,p):
        if ((i * i) % p == x):
            root = i
    bigroot = root if root > p/2  else  p - root
    
    return bigroot

def binary(n):
    binx = ""
    while(n > 0):
        binx += "0" if (n%2 == 0) else "1";
        n = n // 2
    return binx

def p3mod4(x,n,p):
    binx = binary(n)
    product = 1
    tempx = x
    for i in range (0,len(binx)):
        if i == 0:
            tempx = x
        else:
            tempx = pow(tempx,2,p)
        if binx[i] == '1':
            product *= tempx
    product %= p
    bigroot = product if product > p/2  else  p - product

    return bigroot


# x = 85256449776780591202928235662805033201684571648990042997557084658000067050672130152734911919581661523957075992761662315262685030115255938352540032297113615687815976039390537716707854569980516690246592112936796917504034711418465442893323439490171095447109457355598873230115172636184525449905022174536414781771

# p = 101524035174539890485408575671085261788758965189060164484385690801466167356667036677932998889725476582421738788500738738503134356158197247473850273565349249573867251280253564698939768700489401960767007716413932851838937641880157263936985954881657889497583485535527613578457628399173971810541670838543309159139


# x = 1203
# p = 1223
# n = (p+1)/4

# d
# #print((p+1)/4)



# print(p3mod4(x,n,p))
# z = p3mod4(x,n,p)

# print(p-z)


# # x = 5507
# # n = 2435
# # p = 9739
# # ans = p3mod4(x,n,p)
# # def tryy(ans,y,x):

# #     if pow(ans,2) % y == x:
# #         return True
# #     return False

# # print(tryy(ans,p,x))
# # print(x//p)