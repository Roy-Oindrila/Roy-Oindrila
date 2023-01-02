import csv

header = ['Batch ID', ' Batch Name', 'Department Name', 'List of Courses','List of Students']
data = [
    ['CSE22', 'CSE 2022-26', 'CSE', 'C001:C002','CSE2201'],
    ['CSE21', 'CSE 2021-25', 'CSE', 'C001:C002','CSE2101'],
    ['ECE22', 'ECE 2022-26', 'ECE', 'C002','ECE2201:ECE2202'],
    ]

with open('Batch.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)
    f.close()

with open('Batch.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(line)
    f.close()
    quit()