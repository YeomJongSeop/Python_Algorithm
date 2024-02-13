# 문자열 데이터 받기
input_data = input()

input_list = list(input_data)


input_list.sort()

# 리스트 컴프리헨션으로 알파벳 정렬
sorted_alphabet_list = [ alphabet for alphabet in input_list if alphabet >= 'A' ]
sorted_numbers_list = [ int(num) for num in input_list if num < 'A']

num_total = sum(sorted_numbers_list)



sorted_alphabet_list.append(num_total)

for i in sorted_alphabet_list:
    print(i,end='')
