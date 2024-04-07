# -*- coding: utf-8 -*-
import csv

# < 代表向左對齊，<3 代表向左對齊並佔位3
# 這代表輸出一個表頭，適用於終端輸出查看，實務上不需要
print("{0:<3}{1:<5}{2:<4}{3:<4}{4:<5}".format("", "姓名", "總分", "平均", "分數"))
with open("scores.csv", encoding="utf-8") as csvfile:
    x = 0
    for row in csv.reader(csvfile):

        if x > 0:
            total_sum = int(row[1]) + int(row[2]) + int(row[3])
            score = round(total_sum / 3, 1)

            if score >= 80:
                level = "A"
            elif 60 <= score < 80:
                level = "B"
            elif 50 <= score < 60:
                level = "C"
            else:
                level = "D"

            print(
                "{0:<3}{1:<5}{2:<5}{3:<6}{4:<5}".format(
                    x, row[0], total_sum, score, level
                )
            )

        x += 1
