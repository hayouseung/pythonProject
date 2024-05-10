import random

def number_list():
    results = []
    while len(results) < 6:
        number = random.randint(1, 45)
        if number not in results:
            results.append(number)
    results.sort()
    return results

print(f"생성된 로또 번호는 {number_list()}입니다.")
