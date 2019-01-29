import csv

def open_csv():
    with open('Notebooks/Datasets/titanic.csv') as csv_file:
        count = 0
        cv = csv.reader(csv_file)
        for i in cv:
            if (i[1] == "0") and (i[4] == "female"):
                count += 1
        return count
print("Checking the number of females who died on the Titanic...")
print(open_csv())
# import pandas as pd
#
# df = pd.read_csv('titanic.csv')
# df.head()
# df["Sex"] == "female"
# df[df["Sex" == "female"]]
# df[(df["Sex"] == "female") && (df["Survived"] == 1)]
# len(df[(df["Sex"] == "female") && (df["Survived"] == 1)] )
