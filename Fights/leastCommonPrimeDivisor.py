def leastCommonPrimeDivisor(a, b):
    x=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
    c=-1
    for i in x:
        if a%i==b%i==0:
            return c
    return c
