def consecutive_sum(start, end):

    if start == end:
        return start
        
    else:
        return consecutive_sum(start, ((start+end) // 2)) + consecutive_sum( ((start+end) // 2)+1, end)
        
        
    # 여기에 코드를 작성하세요

# 테스트 코드
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))