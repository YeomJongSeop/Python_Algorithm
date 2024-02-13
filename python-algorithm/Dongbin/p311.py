N = int(input()) # 모험가 수 int 형태로 받음
data = list(map(int,input().split())) # 모험가 수의 공포도 입력

data.sort # fear_list.sort # 공포도 오름차순으로 정렬(낮은 순부터 만들어야 그룹을 최대한 많이 만듬

cnt = 0 # 총 그룹 숫자
group_mem = N # 그룹 구성원



# 그룹을 최소 인원부터 구성하되 공포도 만큼 인원을 구성해야함, 인원을 구성 했으면 그 인원만큼 빼주고 다음 공포도 만큼 그룹을 만듬
for i in range(N):
    if data[i] <= group_mem:
        group_mem -= data[i]
        cnt += 1
    else: break

print(cnt)