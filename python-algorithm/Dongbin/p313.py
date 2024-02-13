

S = input()
#첫 문자열 숫자로 변경해서 result에 넣어줌
result = int(S[0])

# 2번 index인 1부터 result 와 곱셉 아니면 덧셈을 실행
for i in range(1,len(S)):
    num = int(S[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

