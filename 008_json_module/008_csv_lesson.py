import csv

# with open('test_csv.csv', "r", encoding='utf8') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         with open('test2.csv', 'w', encoding='utf8') as csv_write:
#             csv_filew = csv.writer(csv_write, delimiter='-', lineterminator='\n')
#             for line in csv_reader:
#                 csv_filew.writerow(line)
with open("test_csv.csv",'r', encoding='utf8') as csv_fileDic:
    dict_reader = csv.DictReader(csv_fileDic)

    with open("test2.csv",'w', encoding='utf8') as csv_fileDic2:
        fieldnames = ['Name','Date of birth','Town']
        dict_writer = csv.DictWriter(csv_fileDic2, delimiter=',', fieldnames=fieldnames)
        dict_writer.writeheader()
        for line in dict_reader:
            dict_writer.writerow(line)

        # next(csv_reader)
        # for line in csv_reader:
        #     print(line)