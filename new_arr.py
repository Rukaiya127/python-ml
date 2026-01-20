from functools import reduce
def concatenate_arrays(A,B):
    return reduce(lambda x,y : x + [y], B + A , [])

#Input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#Function call
C = concatenate_arrays(A,B)

#Output
print(*C)
