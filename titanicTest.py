import csv

def open_csv():
    with open('Notebooks/Datasets/titanic.csv') as csv_file:
        female_count = 0
        male_count = 0
        female_dead_count = 0
        male_dead_count = 0
        dead_count = 0
        total = 0
        cv = csv.reader(csv_file)
        for i in cv:
            total += 1
            if i[1] == "0":
                dead_count += 1
            if i[4] == "female":
                female_count += 1
            if i[4] == "male":
                male_count += 1
            if (i[1] == "0") and (i[4] == "female"):
                female_dead_count += 1
            if (i[1] == "0") and (i[4] == "male"):
                male_dead_count += 1
        female_dead_percentage = float(female_dead_count)/float(female_count)
        male_dead_percentage = float(male_dead_count)/float(male_count)
        print("Female total: " + str(female_count))
        print("Male total: " + str(male_count))
        print("Female dead: " + str(female_dead_count))
        print("Male dead: " + str(male_dead_count))
        print("Female dead percentage: " + str(female_dead_percentage))
        print("Male dead percentage: " + str(male_dead_percentage))
        print("Female survivors: " + str(female_count-female_dead_count))
        print("Male survivors: " + str(male_count-male_dead_count))
        print("Total survivors: " + str(total-dead_count))
        print("Total dead: " + str(dead_count))
        print("All on the Titanic: " + str(total))
        return female_dead_count
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
