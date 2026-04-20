import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")
# 1. The Imports
# gspread: The main library that makes interacting with Google Sheets easy (instead of writing raw API requests).

# Credentials: A class from Google's official auth library used to verify that your program has permission to access your Google account.

# 2. Defining the "Scope"
# The SCOPE list defines exactly what your program is allowed to do. Think of this as a digital badge that tells Google:

# .../auth/spreadsheets: "I want to read and write to spreadsheets."

# .../auth/drive.file: "I want to access files created by this app."

# .../auth/drive: "I want full access to the Google Drive."

# 3. Authentication (The creds.json)
# Python

# CREDS = Credentials.from_service_account_file("creds.json")
# This line looks for a file named creds.json in your project folder. This file contains your Service Account key (private information like your client email and private key).

# SCOPED_CREDS: This applies the permissions (the SCOPE) to those credentials.

# 4. Authorizing the Client
# Python

# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# This line actually logs you in. It creates a "client" object (GSPREAD_CLIENT) that you will use for all future interactions with Google Sheets.

# 5. Opening the Spreadsheet
# Python

# SHEET = GSPREAD_CLIENT.open("love_sandwiches")
# Finally, the code searches your Google Drive for a spreadsheet titled "love_sandwiches". If found, it assigns that entire spreadsheet to the variable SHEET.

# Important Prerequisites
# For this code to work without crashing, you must have completed these steps:

# Enable APIs: You must have enabled the Google Drive API and Google Sheets API in the Google Cloud Console.

# The JSON File: You must have downloaded your Service Account key and renamed it to creds.json.

# Share the Sheet: You must share your Google Sheet ("love_sandwiches") with the client_email found inside your creds.json file, otherwise you will get a "Spreadsheet not found" error.


def get_sales_data():

    print("please enter sales data from your last market")
    print("Data should be six numbers sepaarated by commas\n")
    data_str = input("Enter your data here: ")
    print(f"the data provided is {data_str}\n")
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    try:
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"invalid data: {e}, please try again. \n")


get_sales_data()
