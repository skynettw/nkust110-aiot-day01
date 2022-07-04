import csv
with open("10706.csv", "r", encoding="utf-8") as fp:
    csv_reader = csv.reader(fp)
    data = list(csv_reader)
for row in data:
    if "楠梓" in row[1]:
        print(row[2], row[3], row[4])
#作業：建立此資料中所有的姓氏人口數（不分性別）的總排行