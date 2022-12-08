import csv
with open ('dq_unisex_names.csv') as r:
    reader_r = csv.reader(r)
    headers = next(reader_r)
    rows = []
    for row in reader_r:
        rows.append(row)
    print(headers)
    print(rows)
    for row in rows:
        row[1] = float(row[1])
    print("After converting to float: ")
    print(rows)
