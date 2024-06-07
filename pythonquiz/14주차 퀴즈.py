def menu_choice():
    menu = ["냉면", "볶음밥", "피자", "짜장면"]
    while True:
        try:
            a = input("메뉴 번호를 입력해 주세요: ")
            return menu[int(a) - 1]
        except ValueError:
            print("메뉴에 적힌 숫자만 입력 가능 합니다. 다시 입력해 주세요.")
        except IndexError:
            print("메뉴에 없는 번호 입니다. 다시 입력해 주세요.")


print("메뉴 목록: 1. 냉면, 2. 볶음밥, 3. 피자, 4. 짜장면")
print(f"선택한 메뉴는 {menu_choice()}")
