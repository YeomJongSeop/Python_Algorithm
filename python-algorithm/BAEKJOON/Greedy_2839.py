# N(설탕 키로수)를 입력 받음
n = int(input())




def find_min_bags(n):
    # 5키로 봉지 최대 사용
    five_kg_bags = n // 5
    # 
    while five_kg_bags >= 0:
        # 남은 무게
        remain_weight = n  - (five_kg_bags * 5)
        
        # 남은 무게가 3kg 봉지로 나누어 떨어지는 경우
        if remain_weight % 3 == 0:
            three_kg_bags = remain_weight // 3
            return five_kg_bags + three_kg_bags     # 총 봉지 개수
        
        # 5kg 봉지 사용 줄임
        five_kg_bags -= 1

    # 정확히 N킬로그램 못 만들 경우
    return -1



print(find_min_bags(n))





