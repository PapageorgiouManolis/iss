import csv

with open('../data/data.txt') as f:
    lines = f.read().splitlines()

print(len(lines))
new_rows = list()
for line in lines:
    datetime, latitude, longtitude = line.split(',')

    new_rows.append(line.split(','))

print(len(new_rows))
print(new_rows[10])

with open('../data/data.csv', mode='w') as csv_file:
    file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in new_rows:
        file_writer.writerow(row)
