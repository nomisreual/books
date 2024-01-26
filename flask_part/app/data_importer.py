import csv

def read_csv(file_path):
    received_data = []

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            received_data.append(row)
    
    return received_data

file_path = 'books_data.csv'
extracted_data = read_csv(file_path)
tags_list = ["Book: ", "Author: ", "Birth Date: ", "Publication: ", "Copies Sold: ", "ISBN: ", "Publisher: ", "Address: "]
