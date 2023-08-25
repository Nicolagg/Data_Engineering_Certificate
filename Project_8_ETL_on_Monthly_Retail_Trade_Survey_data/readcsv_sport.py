import csv

# Open file
with open('csv/sport.csv') as csv_file:
    
    # Read CSV file
    csv_reader = csv.reader(csv_file, delimiter=';')

    # Loop through data
    
    for row  in csv_reader:
        print(row)