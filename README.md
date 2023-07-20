To run the application, you need to install the required dependencies, 'datetime', and 'python-dotenv'.

Before running the application, you must add your own keys and endpoints to the '.env' file.
Ensure that your '.env' file contains the following necessary information:

# TWILIO
ACCOUNT_SID_ENV=your sid ;
AUTH_TOKEN_ENV=your token ;
FROM_ENV=your from number ;
TO_ENV=your to number

# SHEETY
SHEETY_ENDPOINT_ENV=your sheety endpoint ;
SHEETY_TOKEN_ENV=your sheety token

# TEQUILA
TEQUILA_API_ENV=your tequila api key

Additionally, you need to create a google sheets file with a formula
like the one linked: [Google Sheets](https://docs.google.com/spreadsheets/d/1EI_GoLOoTVZCF3lok5WWVLjhTf5CJ_UbmerEyUCQxgM/edit#gid=0)


I have developed an application that allows users to register and save their information to the database on the Repl.it website. [Cheap Flights User Registration.](https://replit.com/@jakubwawrzyczek/cheap-flights-user-registration#data_manager.py)

Please note that this application is specifically designed for adding new users to the database used by the flight-checking and notification program. It complements the main functionality of the program.

I created this application while taking the Python course on Udemy with Angela Yu.
