num = 1
summary = 1

for i in range(1, 3+1):
    for j in range(1, 3+1):
        print(num, end='\t')
        num += 1
    print()


summary += num - 1
summary += int(summary * 0.5)

print("Сумма чисел главное диагонали равна:", summary)
