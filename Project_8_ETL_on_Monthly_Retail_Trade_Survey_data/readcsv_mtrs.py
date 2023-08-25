import csv

# Open file
with open('csv/2020.csv') as csv_file:
    
    # Read CSV file
    csv_reader = csv.reader(csv_file, delimiter=';')

    # Loop through data
    
    for row in csv_reader:
        print(row)
