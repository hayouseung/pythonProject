n = int(input("몇 단까지 출력할까요?"))

a = 1
b = 1
while a <= n:
    print("-" * 6, "[", a, "단", "]", "-" * 6)
    while b <= 19:
        print(a, "x", b, "=", a*b)
        b = b+1
    a = a+1
    b = b-19
