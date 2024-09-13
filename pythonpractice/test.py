n = int(input("몇 번째로 작은 소수를 구할지 입력하세요: "))
prime_number_list = []
a = 2
k = 1
while n >= 1:
    while a < k:
        if k % a == 0:
            break
        a = a + 1
    if a == k:
        prime_number_list.append(k)
    if len(prime_number_list) == n:
        print(f"{n}번째로 작은 소수: {prime_number_list[n-1]}")
        break
    a = 2
    k = k + 1
else:
    print("자연수만 입력이 가능합니다. 다시 실행해 주세요.")
print(f"{n}번째까지 소수들의 합: {sum(prime_number_list[0:n-1])}")
