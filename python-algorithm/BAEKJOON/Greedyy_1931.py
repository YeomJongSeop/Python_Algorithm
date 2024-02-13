# 회의의 수 n 설정
n = int(input())


time_list =[]


for i in range(n):
    start, end = map(int, input().split())
    time_list.append((start, end))

# 끝나는 시간을 순서대로 정렬해야 최대한 많은 회의를 할 수 있음, 아래는 끝나는 시간을 기준으로 오름차순 시킨 코드이다.
sorted_time_list = sorted(time_list,  key=lambda x: (x[1], x[0]) ) # time_list.sort(key=lambda x: (x[1]) 와 동일한데 같을 경우 x[0]을 기준으로 겹치면 시작시간이 빠른 순으로 추가 정렬

# time_list.sort(key=lambda x: x[1],reverse= True) reverse 쓰고 싶으면 이런식으로 뒤에다 써줌  time_list.sort(key=lambda x: (x[1], reverse = True)

last_end_time = 0
count = 0

for time in sorted_time_list:
    start_time ,end_time = time
    if start_time >= last_end_time:
        count +=1
        last_end_time = end_time

print(count)
    



