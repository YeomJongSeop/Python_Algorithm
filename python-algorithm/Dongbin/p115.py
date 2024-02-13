# 현재 나이트의 위치 입력받기(column은 문자 알파벳으로 입력 받으니 숫자로 변환해줘야함)
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

count = 0 
# dx, dy로 방향 정의하기
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, 2, -2, 2, -2, -1, 1]

for i in range(len(dx)):
    next_row = row + dx[i]
    next_column = column + dy[i]
    if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <=8:
        count += 1

        
# 8가지 방향에 대해 각 위치로 이동 가능한지 확인

# for step in steps:
#     # 이동하고싶은 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치 이동 가능하면 카운트 증가
#     if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <=8:
#         count += 1

print(count)