n = int(input("몇 단까지 출력할까요?"))

for a in range(1, n+1):
    print("-"*6, "[", a, "단", "]", "-"*6)
    for b in range(1, 20):
        print(a, "x", b, " =", a*b)
