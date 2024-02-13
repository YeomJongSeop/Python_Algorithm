# n 입력받기

n = int(input())

# 시간을 정수 형태의 리스트로 입력 받기
time_list = list(map(int, input().split()))

# 오름차순으로 정렬
time_list.sort()

# 번호대로의 시간을 기록할 캐시 생성
cache =[]

# 걸리는 시간 생성
time_count = 0


for i in time_list:
    time_count += i
    cache.append(time_count)


print(sum(cache))
