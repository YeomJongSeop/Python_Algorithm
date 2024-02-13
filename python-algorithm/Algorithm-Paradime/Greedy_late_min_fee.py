def min_fee(pages_to_print):
    # 여기에 코드를 작성하세요
    pages_to_print.sort()
    i = 0
    fee = 0
    cache = []

    while i < len(pages_to_print): # 중복해서 더하는 것을 구현해야함
            fee += pages_to_print[i]
            i += 1
            cache.append(fee)
    return sum(cache) # sum 함수를 이용해 리스트안 요소들 다 합함


# 테스트 코드
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))