import csv


def read_csv(file_path):

    """ Read a csv file and yielding each line. Hence,
    the whole file is not loaded into memory all at once.
    """

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row
