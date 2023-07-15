You need to install datetime, and python-dotenv.

If you want the application to work, you must add your own keys and
endpoints to the .env file.


You need the following in your '.env' file for it to work:

# TWILIO
ACCOUNT_SID_ENV=your sid
AUTH_TOKEN_ENV=your token
FROM_ENV=your from number
TO_ENV=your to number

# SHEETY
SHEETY_ENDPOINT_ENV=your sheety endpoint
SHEETY_TOKEN_ENV=your sheety token

# TEQUILA
TEQUILA_API_ENV=your tequila api key

Additionally, you need to create a google sheets file with a formula
like the one linked: https://docs.google.com/spreadsheets/d/1EI_GoLOoTVZCF3lok5WWVLjhTf5CJ_UbmerEyUCQxgM/edit#gid=0


In addition, I created an application that allows you to save new users to the database on the repl.it website.
I am attaching the link:
https://replit.com/@jakubwawrzyczek/cheap-flights-user-registration#data_manager.py

It is connected to the database used by the program checking flights and sending notifications, but it is used only to add new users

I hope that's all you need to know!

Program was made while doing Udemy Angela Yu Python course
