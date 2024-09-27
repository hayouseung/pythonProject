# Quiz 1
def quiz1():
    user_input = input("문자열을 입력하세요: ")
    if user_input == "안녕하세요":
        print("반갑습니다")
    else:
        print("인사를 먼저하세요.")

# Quiz 2
def quiz2():
    user_input = int(input("값을 입력하세요: "))
    result = user_input + 100
    if result >= 150:
        print(result)
    else:
        print("값이 부족합니다.")

# Quiz 3
def quiz3():
    numbers = [100, 200, 300]
    result = []
    for number in numbers:
        result.append(number * 1.1)
    print(result)

# Quiz 4
def quiz4():
    numbers = [3, 100, 23, 33, 72, 94]
    result = []
    for number in numbers:
        if number % 3 == 0:
            result.append(number)
    print(result)

# Quiz 5
def quiz5():
    counter = 1
    while counter <= 1000:
        print(f"대기번호: {counter}")
        counter += 1

# Quiz 6
def quiz6():
    sum_of_odds = 0
    number = 1
    while number <= 100:
        if number % 2 != 0:
            sum_of_odds += number
        number += 1
    print(sum_of_odds)

quiz1()
quiz2()
quiz3()
quiz4()
quiz5()
quiz6()
