#   IDEA: A database (DB) will be used as an example. It should be a .json file as one of the instances in the db.

import getpass
import psycopg2
import json
import pandas
from datetime import datetime

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="::1",         # If you need to know your localhost, type this: psql -h localhost -U postgres -c "SELECT inet_server_addr();"
    database="FLOWERS_db",
    user="postgres",    # If you need to know your localhost, type this:
    password=getpass.getpass("Enter your database password: ")
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the data to be inserted
flower_name = "Iris"
timestamp = datetime.now()
json_file_path = "C:/Users/berna/OneDrive/VirtualShare/UnstructuredDB/DBIntegration/iris.json"

# Read the JSON data from the file
with open(json_file_path) as file:
    json_data = json.load(file)

# Convert the json_data to a JSON string
json_data_str = json.dumps(json_data)

print(json_data_str)

# Prepare the SQL query
#insert_query = '''
    #INSERT INTO Flowers ("Flower_name", Timestamp, Json_data)
    #VALUES (%s, %s, %s);
#'''

# Execute the insert query
#cursor.execute(insert_query, (flower_name, timestamp, json_data_str))




# Commit the changes to the database
conn.commit()

# Close the cursor and database connection
cursor.close()
conn.close()