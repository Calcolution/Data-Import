import requests
import pyodbc
import json

# Prompt user for API URL
api_url = input("Enter API URL: ")

# Request data from API
try:
    response = requests.get(api_url)
    response.raise_for_status()
    file_type = response.headers['Content-Type'].split('/')[-1]
    if file_type :
        data = response.json()['dataset']
    else:
        print(f"Error: unsupported file type: {file_type}")
        exit()
except requests.exceptions.RequestException as e:
    print("Error fetching data from API:", e)
    exit()

# Prompt user for database connection details
server = input("Enter server name: ").strip() # 'calcolution.database.windows.net' 
database = input("Enter database name: ").strip() # 'calcolution' 
username = input("Enter username: ").strip() # 'calcolution' 
password = input("Enter password: ").strip() # '123*testinG' 

# Connect to database
if server and database and username and password:
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
        )
    except pyodbc.Error as e:
        print("Error connecting to database:", e)
        exit()

    # Create table if it doesn't exist
    try:
        cursor = connection.cursor()
        cursor.execute("""
            IF OBJECT_ID('table_name', 'U') IS NULL
            BEGIN
                CREATE TABLE table_name (
                    [{}] [nvarchar](50) NULL
                );
            END;
        """.format('] nvarchar(50) NULL, ['.join(data['column_names'])))
        connection.commit()
    except pyodbc.Error as e:
        print("Error creating table:", e)
        exit()

    # Insert data into database
    try:
        cursor = connection.cursor()
        if file_type:
            for row in data['data']:
                columns = ', '.join(['[' + col + ']' for col in data['column_names']])
                values = ', '.join(['?' for i in range(len(data['column_names']))])
                cursor.execute(f"INSERT INTO table_name ({columns}) VALUES ({values})", tuple(row))
        connection.commit()
    except pyodbc.Error as e:
        print("Error inserting data into database:", e)
        exit()

    print("Data imported successfully!")
else:
    print("Please input all details.")