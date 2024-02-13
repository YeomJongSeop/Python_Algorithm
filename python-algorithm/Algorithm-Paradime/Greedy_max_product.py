def max_product(card_lists):
    # 여기에 코드를 작성하세요
    i = 0
    max_p = 1 # 초기값을 0으로 잡으면 0으로만 나오니 1로 해야함

    while i < len(card_lists):
        max_p *= max(card_lists[i])
        i += 1
    return max_p



# 테스트 코드
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))
