import csv

header = ['Department ID', 'Department Name', 'List of Batches']
data = [
    ['CSE', 'Computer Science and Engineering',  'CSE22:CSE21'],
    ['ECE', 'Electronics and Communication Engineering','ECE22'],
    ]

with open('Department.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)
    f.close()

with open('Department.csv', encoding="utf8") as f:
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