# data_handling.py
import csv
import json

# Write data to CSV file
def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Read data from CSV file
def read_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return [row for row in reader]

# Write data to JSON file
def write_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Read data from JSON file
def read_from_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Test cases for data handling
if __name__ == "__main__":
    # uncomment the following code in order to reinitlize the exercise sequence
    #csv_data = [['Name', 'Age'], ['Alice', 28], ['Bob', 35], ['Charlie', 22]]
   # write_to_csv("data.csv", csv_data)
    read_csv_data = read_from_csv("data.csv")
    print("CSV Data:", read_csv_data)

   # json_data = {"students": [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 35}]}
   # write_to_json("data.json", json_data)
    read_json_data = read_from_json("data.json")
    print("JSON Data:", read_json_data)

