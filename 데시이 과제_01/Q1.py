import csv

f = open("heat_wave.csv", 'r', encoding="cp949")
data = csv.reader(f)

# 아래부터 솜솜이가 작성해야 할 부분

# 헤더 5줄 건너뛰기
for i in range(5):
    next(data)

# 변수 초기화 해주기
year = ''
location = ''
start_date = ''
end_date = ''
max_duration = 0  # 가장 긴 지속일수 저장

for row in data:
    if row[4] != '':  # 지속일수가 존재하는지 확인
        current_duration = int(row[4])
        if current_duration > max_duration:
            max_duration = current_duration
            year = row[0]
            location = row[1]
            start_date = row[2]
            end_date = row[3]
            duration = int(row[4])

# 시작일/종료일에서 월, 일을 분리
start_month = start_date[5:7]
start_day = start_date[8:]
end_month = end_date[5:7]
end_day = end_date[8:]


print("폭염 지속일수가 가장 길었던 연도:", year + "년")
print("해당 지점:", location)
print("폭염 시작일:", start_month + "월", start_day + "일")
print("폭염 종료일:", end_month + "월", end_day + "일")
print("지속일수:", str(max_duration) + "일")

f.close()