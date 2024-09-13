class Beverage:
    def __init__(self, name, count):
        self.menu = {"커피": 3000, "녹차": 2500, "아이스티": 3000}
        self.name = name
        self.count = count
        self.total = 0

    def calculate(self):
        if self.name in self.menu:
            self.total += self.menu[self.name] * self.count
            return self.total
        else:
            return "음료 이름이 잘못 입력되었습니다. 다시 입력해 주세요."


choice_beverage = input("주문할 음료를 선택해 주세요(커피/녹차/아이스티): ")
choice_count = int(input("주문할 음료의 개수를 입력해 주세요: "))
order = Beverage(choice_beverage, choice_count)
print(f"총 금액: {order.calculate()}원")
