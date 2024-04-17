fruits = ["사과", "바나나", "딸기"]

for fruit in fruits:
    print(fruit)

dic = {"과일": "사과", '숫자': 1, '사람 이름': '홍길동'}

for i in dic:
    print(i, dic[i])

hangle = "가나다라마바사"

for j in hangle:
    print(j)

for k in range(0, 10):
    print(k)

content = "사과 같은 배"

while content == "사과":
    print("사과입니다.")
else:
    print("사과가 아닌 다른 것이므로 코드 실행을 중지합니다.")

number = 1

while number < 5:
    print(number)
    number = number + 1

else:
    print("number 변수가 5이상이면 종료합니다.")

number = 1

while number < 5:
    print(number)
    break
    number = number + 1