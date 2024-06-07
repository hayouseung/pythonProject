class Kiosk:
    def __init__(self, num):
        self.menu = ["냉면", "볶음밥", "피자", "짜장면"]
        self.num = num
        self.count = 0

    def menu_choice(self):
        try:
            return self.menu[int(self.num) - 1]
        except ValueError:
            return "메뉴에 적힌 숫자만 입력 가능 합니다."
        except IndexError:
            return "메뉴에 없는 번호 입니다."


print("메뉴 목록: 1. 냉면, 2. 볶음밥, 3. 피자, 4. 짜장면")
menu_number = input("메뉴 번호를 입력해 주세요: ")
print(Kiosk(menu_number).menu_choice())
