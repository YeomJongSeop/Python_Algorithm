def min_coin_count(value, coin_list):
    # 여기에 코드를 작성하세요
    coin_list.sort(reverse=True)
    i = 0
    count = 0 #동전개수

    # while i < len(coin_list): 
    #     share = value // coin_list[i] # 몫으로 동전개수 파악
    #     remain = value % coin_list[i] # 나머지 값을 나중에 value값으로
    #     count += share # 동전개수에 넣어줌
    #     i=i+1 # 다음 동전으로
    #     value = remain 

    for i in coin_list:
        count += value // i
        value %= i 

    return count



# 테스트 코드
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))