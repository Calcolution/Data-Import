# Import Excel to Azure SQL Python Script

This Python script imports data from an Excel file into an Azure SQL database. The script reads each worksheet in the Excel file, creates a table for each worksheet, and imports the data into the corresponding table.

## Prerequisites

- Python 3.x
- Required packages: `pandas`, `pyodbc`, `openpyxl`
- ODBC Driver 17 or 18 for SQL Server
- An Azure SQL database

## Instructions

1. Make sure you have installed the required packages by running the following command:

   ```
   pip install pandas pyodbc openpyxl
   ```

2. Check if you have ODBC Driver 17 or 18 for SQL Server installed. If you have version 18, keep the driver variable as is. If you have version 17, change the driver variable in the code to:

   ```python
   driver = '{ODBC Driver 17 for SQL Server}'
   ```

3. Make sure not to use spaces in the Excel file name, as this may cause issues when creating tables in the Azure SQL database. It's best to choose a file name without spaces.

4. Make sure to provide the correct path to the Excel file in the `excel_file_path` variable. To avoid confusion, it's recommended to keep the Excel file in the same folder as the Python script.

5. Ensure your IP is added to the Azure SQL Server firewall rules to allow access to the database.

6. Run the Python script. The script will create a table for each worksheet in the Excel file and import the data into the corresponding table in the Azure SQL database. If there are any errors, the script will print them to the console.

## Notes

- The script assumes that each worksheet in the Excel file has a header row with column names.
- The script replaces spaces in column names with underscores.
- The script handles connection errors and issues when creating tables and inserting data into the tables.