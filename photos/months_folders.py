import os


def create_month_folders(root, year):

    year_path = os.path.join(root, year)

    if not os.path.exists(year_path):
        os.makedirs(year_path)

    print("Folder {} created.".format(year_path))

    for i in range(1, 13):
        month_path = os.path.join(year_path, "%s-%02d" % (year, i))

        if not os.path.exists(month_path):
            os.makedirs(month_path)

        print("Folder {} created.".format(month_path))


create_month_folders("/Users/rossellabozzini/Pictures/Lightroom", "2019")
