import csv

# Open the CSV file
with open('resistors.csv', 'r') as file:  # Replace 'data.csv' with the path to your CSV file
    reader = csv.reader(file)
    
    # Skip the header
    next(reader)

    # Read all rows into a list
    values = [row[0] for row in reader]

# Print 16 values per line
for i in range(0, len(values), 16):
    print(' '.join(values[i:i+16]))