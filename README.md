# Data-Import

Here's a step-by-step guide to help you install the required packages, set up the environment, and run the code to import Excel data into Azure SQL.

### Step 1: Install Python
1. Download and install Python 3 from the official website: https://www.python.org/downloads/
2. Make sure to check the "Add Python to PATH" option during installation.
3. Open a terminal or command prompt and run `python --version` to check the successful installation. You should see the version of Python you just installed.

### Step 2: Install Required Packages
1. Open a terminal or command prompt and run the following command to install the necessary packages:
   ```
   pip install pandas pyodbc openpyxl
   ```

### Step 3: Set up an Azure SQL Database
1. Sign in to the Azure portal: https://portal.azure.com/
2. Create an Azure SQL Database by following the official documentation: https://docs.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart?tabs=azure-portal
3. Replace the following variables in the Python code with your own Azure SQL Database connection details:
   ```python
   server = 'your_server.database.windows.net'
   database = 'your_database'
   username = 'your_username'
   password = 'your_password'
   driver = '{ODBC Driver 17 for SQL Server}'
   ```

### Step 4: Install ODBC Driver for SQL Server
1. Download and install the ODBC Driver for SQL Server from the official website: https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
2. Make sure to choose the appropriate driver version (x86 or x64) based on your system architecture.

### Step 5: Prepare the Excel File
1. Make sure the Excel file you want to import into Azure SQL is in the `.xlsx` format and each worksheet has a header row with column names.
2. Replace the `excel_file_path` variable in the Python code with the path to your Excel file:
   ```python
   excel_file_path = 'your_excel_file.xlsx'
   ```

### Step 6: Run the Python Script
1. Open a terminal or command prompt, navigate to the folder containing the script, and run the following command:
   ```
   python ImportExcelToSQL.py
   ```
2. The script will create a table for each worksheet in the Excel file and import the data into Azure SQL. If there are any errors, the script will print them to the console.