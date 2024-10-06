# Importing necessary libraries
import pymongo
import sys
import csv

# Setting a limit for the field size to 2147483647
csv.field_size_limit(2147483647)

# Connecting to the local MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["enron"]
collection = db["enronmails"]

# Importing the reader function from the csv library
from csv import reader

# Opening the 'emails.csv' file in read mode
with open('emails.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)

    # Iterating through each row of the CSV file
    for row in csv_reader:
        if "_sent_mail" in str(row[0]):
            # Creating a dictionary to store the email data
            email_data = {}

            # Storing the contents of the first column in the 'file' key of the dictionary
            email_data['file'] = row[0]

            # Storing the contents of the second column in the 'message' key of the dictionary
            email_data['message'] = row[1]
        
            # Inserting the email data into the enronmails10 collection
            collection.insert_one(email_data)
