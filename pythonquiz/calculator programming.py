a = float(input("첫째 항을 입력하세요: "))
r = float(input("공비를 입력하세요: "))
start = int(input("몇 번째 항부터 더할지 입력하세요: "))
end = int(input("몇 번째 항까지 더할지 입력하세요: "))

if r == 1:
    sequence_sum = a*(end-start+1)
else:
    sequence_sum = (a*(1-r**end)/(1-r)) - (a*(1-r**(start-1))/(1-r))
for k in range(start, end + 1):
    print(f"{k}번째 항: {a*r**(k-1)}")
print(f"{start}번째 항부터 {end}번째 항까지의 합은 {sequence_sum}입니다.")
