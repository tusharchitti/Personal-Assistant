import csv

with open('test.txt', "rb") as infile, open('test.csv', 'wb') as outfile:
    in_txt = csv.reader(infile, delimiter = ',')
    out_csv = csv.writer(outfile)
    out_csv.writerow(('emotion', 'sentiment'))
    out_csv.writerows(in_txt)
