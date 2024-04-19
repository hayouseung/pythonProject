numbers = [[1,2,3], [4,5,6], [7,8,9]]
results = []
for a in range(0,3):
    for b in range(0,3):
        if (numbers[a][b] % 2) == 0:
            results.append(numbers[a][b])
print(results)
