# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2] , my_list[index1] 
    
    ''' #기존 다른 언어는 임시변수에 값 넣어두고 해야하지만 파이썬은 한줄로 가능
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

    '''

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
            pivot = big # pivot의 인덱스는 설정
            break
        else: # pivot 보다 가르키는 값이 작으면 big의 인덱스와 i인덱스의 값 바꾸고 1씩 값 늘려줌
            swap_elements(my_list, big, i)
            big += 1
            i += 1 


    return pivot
   


# 테스트 코드 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 코드 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)