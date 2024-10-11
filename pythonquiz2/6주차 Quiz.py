# Quiz 1
class User:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def info(self):
        print(f"가입하신 계정의 이름은 {self.name}이며, 나이는 {self.age}, 그리고 연락처는 {self.phone_number}입니다.")


a = User("하유승", "23", "010-1234-5678")
a.info()


# Quiz 2
def check_length_of_message(message):
    if len(message) <= 20:
        return "50원"
    else:
        return "100원"


mail = input("문자 메시지를 입력하세요: ")
print(check_length_of_message(mail))
