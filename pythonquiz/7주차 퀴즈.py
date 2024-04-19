numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
results = []
for a in numbers:
    for b in a:
        if b % 2 == 0:
            results.append(b)
print(results)
