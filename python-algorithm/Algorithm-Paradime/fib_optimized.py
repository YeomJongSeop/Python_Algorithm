def fib_optimized(n):
    current =1
    previous = 0
# 반복문 아래 임시변수 없이 쓰는 법: current, previous = current + previous, current

# 이 구문을 분해하여 설명하면 다음과 같습니다:

# current + previous: 이 부분은 current와 previous의 현재 값의 합을 계산합니다. 이 합산은 피보나치 수열에서 다음 숫자를 생성하는 데 사용됩니다.

# current, previous = ...: 여기서 Python은 오른쪽에 있는 값을 왼쪽의 변수들에 할당합니다. 이 할당은 한 단계로 진행되기 때문에, 모든 오른쪽 값이 계산된 후에 왼쪽의 변수에 할당됩니다.

# ..., current: 이 부분은 현재 current 변수의 값을 previous 변수로 업데이트합니다.

# 전체 구문은 다음과 같은 과정을 수행합니다:

# current 변수는 current와 previous의 합으로 업데이트됩니다. 이는 피보나치 수열의 다음 숫자가 됩니다.
# previous 변수는 이전 current 값으로 업데이트됩니다. 이는 피보나치 수열에서 현재 숫자가 됩니다.


    for i in range(1,n):
        temp = current
        current = current + previous
        previous = temp
    return current


# 테스트 코드
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))