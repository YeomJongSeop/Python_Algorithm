def course_selection(course_list):
    # 수업을 끝나는 시간 기준으로 오름차순 정렬
    sorted_courses = sorted(course_list, key=lambda x: x[1])
    
    # 최종적으로 선택된 수업 리스트
    selected_courses = []
    
    # 마지막으로 선택된 수업의 끝나는 시간
    last_end_time = 0
    
    for course in sorted_courses:
        # 현재 수업의 시작 시간이 마지막으로 선택된 수업의 끝나는 시간보다 크거나 같다면
        if course[0] >= last_end_time:
            # 수업을 선택
            selected_courses.append(course)
            # 마지막으로 선택된 수업의 끝나는 시간을 업데이트
            last_end_time = course[1]
    
    return selected_courses

# 테스트 코드
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
