def min_max(arr):
  get_min = lambda x : min(x) 
  get_max = lambda x : max(x)
  return get_min(arr), get_max(arr)
#Input
N = int(input())
A = list(map(int,input().split()))

#Function call
mn , mx = min_max(A)

#Output
print(mn,mx) 