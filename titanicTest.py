import csv

def open_csv():
    with open('Notebooks/Datasets/titanic.csv') as csv_file:
        count = 0
        cv = csv.reader(csv_file)
        for i in cv:
            if (i[1] == "0") and (i[4] == "female"):
                count += 1
        return count
print(open_csv())
