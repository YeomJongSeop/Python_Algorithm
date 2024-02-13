

N, K = map(int,input().split())


cnt = 0

while N >= K:
    if N % K == 0:
        N /= K 
        cnt += 1
    elif N == 1:
        break
    else: 
        N -=1
        cnt+=1

     
print(cnt)