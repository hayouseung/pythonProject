class Bread:
    def __init__(self, taste, price):
        self.taste = taste
        self.price = price
        self.total = 0
    def sell(self):
        print(f"{self.taste}을 {self.price}에 팔았습니다.")
        self.total += self.price
    def eat(self):
        print(f"{self.taste}을 먹습니다.")


puff_bread = Bread("슈크림", 1000)
puff_bread.sell()
puff_bread.sell()
puff_bread.sell()
puff_bread.sell()
print(puff_bread.total)
