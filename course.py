import csv

header = ['Course ID', 'Course Name', 'Marks obtained(StudentID:Marks-StudentID:Marks-...)']
data = [f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        i
    ['C001', 'Python Programming', 'CSE2201:95-CSE2101:73'],
    ['C002', 'Physics', 'CSE2201:65-CSE2101:78-ECE2201:34-ECE2202:95'],
    ]

with open('Course.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)
    f.close()

with open('Course.csv', encoding="utf8") as f line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(line)
    f.close()
    quit()