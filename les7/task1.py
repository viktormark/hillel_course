import csv

exchange_rate = 36.92

file = open('test_file.csv', 'r')
reader = csv.reader(file)
rows = list(reader)
file.close()

for row in rows[1:]:
    #print(row)
    for i in range(1, len(row)):
        row[i] = str(float(row[i]) * exchange_rate)

file = open('salaries_uah.csv', "w", newline='')
writer = csv.writer(file)
writer.writerows(rows)
file.close()

