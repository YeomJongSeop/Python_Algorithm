# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2] , my_list[index1] 
    

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    pivot = my_list[end] 
    big = start
    i = start


    while i < len(my_list):
        if pivot < my_list[i]: # pivot 보다 가르키는 값이 크면 i의 값만 늘려줌
            i += 1
        elif i == end:
            swap_elements(my_list, big, end)
            pivot = big # pivot의 인덱스는 교환 했으면 마지막 big의 인덱스로 설정
            break
        else: # pivot 보다 가르키는 값이 작으면 big의 인덱스와 i인덱스의 값 바꾸고 1씩 값 늘려줌
            swap_elements(my_list, big, i)
            big += 1
            i += 1 


    return pivot
# 퀵 정렬
def quicksort(my_list, start, end):
    # 여기에 코드를 작성하세요
    if end-start < 1:
        return
    
    pivot = partition(my_list, start, end)

    quicksort(my_list, start ,pivot - 1 )

    quicksort(my_list, pivot + 1, end)

    


# 테스트 코드 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 코드 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 코드 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)