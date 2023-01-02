import csv

header = ['Student ID', 'Name', 'Class Roll Number', 'Batch ID']
data = [
    ['CSE2201', 'Oindrila Roy', '11', 'CSE22'],
    ['CSE2101', 'Puspita Kundu', '01', 'CSE22'],
    ['CSE2201', 'Jishnu Ray', '01', 'CSE22'],
    ['CSE2202', 'Koushiki Ghosh', '02', 'CSE22']
    ]

with open('Students.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)
    f.close()

with open('Students.csv', encoding="utf8") as f:
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