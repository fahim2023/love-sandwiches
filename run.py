import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    """
    Asks the user to input their sales figures from the last market.

    Keeps asking in a loop until the user provides valid data.
    Once valid data is entered, it returns the data as a list of strings.

    Returns:
        list: A list of 6 string values e.g. ['10', '20', '30', '40', '50', '60']
    """
    while True:
        # Prompt the user to enter their sales figures
        print("Please enter sales data from your last market.")
        print("Data should be six numbers separated by commas.\n")

        # Store whatever the user types as a string
        data_str = input("Enter your data here: ")

        print(f"The data provided is: {data_str}\n")

        # Split the string into a list using the comma as a separator
        # e.g. "10,20,30" becomes ["10", "20", "30"]
        sales_data = data_str.split(",")

        # Check if the data is valid before moving on
        if validate_data(sales_data):
            print("Data is valid!")
            return sales_data  # Exit the loop and return the valid data


def validate_data(values):
    """
    Validates the sales data entered by the user.

    Checks two things:
      1. That all values can be converted to integers (no letters or symbols).
      2. That exactly 6 values were provided.

    Args:
        values (list): The list of strings to validate.

    Returns:
        bool: True if the data is valid, False if not.
    """
    try:
        # Try converting every value in the list to an integer
        # If any value isn't a number, this will trigger a ValueError
        [int(value) for value in values]

        # Check that the user entered exactly 6 numbers
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}")

    except ValueError as e:
        # If anything went wrong, print the error and tell the user to try again
        print(f"Invalid data: {e}, please try again.\n")
        return False  # Data is not valid

    return True  # All checks passed, data is valid


def update_sales_worksheet(data):
    """
    Adds the validated sales data as a new row in the 'sales' worksheet.

    Finds the tab named 'sales' inside the Google Spreadsheet
    and appends the data as a new row at the bottom.

    Args:
        data (list): A list of integers to be added as a new row.
                     e.g. [10, 20, 30, 40, 50, 60]
    """
    print("Updating sales worksheet...\n")

    # Access the 'sales' tab inside the spreadsheet
    sales_worksheet = SHEET.worksheet("sales")

    # Add the data as a new row at the bottom of the sheet
    sales_worksheet.append_row(data)

    print("Sales worksheet updated successfully!\n")


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("calculating surplus...")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    surplus = SHEET.worksheet("surplus")
    pprint(stock)
    print(stock_row)


# --- Main Program Flow ---
def main():
    """
    run all program functions
    """

    # Step 1: Ask the user for their sales data and keep asking until it's valid
    data = get_sales_data()

    # Step 2: Convert each value from a string to an integer
    # e.g. ["10", "20"] becomes [10, 20]
    sales_data = [int(number) for number in data]

    # Step 3: Send the cleaned data up to the Google Spreadsheet
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)


print("welcome to love sandwiches data automation")
main()
