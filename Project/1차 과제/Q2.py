import csv
import matplotlib.pyplot as plt

f = open("sr_profit.csv", 'r', encoding="cp949")
data = csv.reader(f)

header = next(data)

# 열 인덱스 딕셔너리 생성
target_cols = {}
for i, col_name in enumerate(header):
    if '경부선' in col_name:
        year_part = col_name.split('년')[0] # '년'을 기준으로 나눠 연도만 추출해옴
        if year_part.isdigit() and int(year_part) % 2 != 0: # 연도가 숫자로만 이루어져있고 홀수 연도여야함 (공집합
            target_cols[year_part] = i # 추출해야 하는 열 인덱스 {'2017': 4, '2019': 10, ...}

# target_cols 딕셔너리에서 key값(연도)만 가져온 후 정렬
sorted_years = sorted(target_cols.keys())

# 각 연도별로 수익 데이터를 저장할 빈 딕셔너리 생성
profits = {y:[] for y in sorted_years}

# 각 연도별 월별 수익값 저장
for row in data:
    for y in sorted_years:
        value = row[target_cols[y]]
        if value != '':
            profits[y].append(int(value))

f.close()

colors = ['r', 'g', 'b', 'k']
markers = ['^', '>', 'v', '<']
months = list(range(1, 13))

# 그래프 그리기
for i, y in enumerate(sorted_years):
    plt.plot(
        months,
        profits[y],
        color=colors[i],
        marker=markers[i],
        linewidth=0.5,
        label=y
    )

plt.xlabel("Month")
plt.ylabel("Profit")
plt.legend()
plt.grid(True)
plt.show()