def binary_search(element, some_list):
    some_list.sort()
    start =0 
    end = len(some_list) - 1

    while start<=end:
        mid =(start +end) // 2 # 중간값

        if some_list[mid] == element: # 위치 반환
            return mid
        elif some_list[mid] > element: # 찾는 요소가 더 작으면 왼쪽을 탐색
            end = mid - 1
        else:                          # 찾는 요소가 더 크면 오른쪽을 탐색
            start = mid + 1
            
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))