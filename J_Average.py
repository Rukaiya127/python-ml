def avg_mean(arr):
    return sum(arr)/len(arr)

#input
N = int(input())
A = list(map(float,input().split()))

#function call

mean_ = avg_mean(A)
print(f"{mean_:.7f}")