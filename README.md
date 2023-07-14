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
like the one linked below:

https://docs.google.com/spreadsheets/d/1EI_GoLOoTVZCF3lok5WWVLjhTf5CJ_UbmerEyUCQxgM/edit#gid=0

I hope that's all you need to know!

Program was made while doing Udemy Angela Yu Python course
