# Amazon_product_availability_tracker
A python script to scrape amazon and check for the avaibility of a product in every 20 - 30 seconds and when the product is available it will ping you with a call.
Apis Used:
1. https://www.twilio.com/
2. https://www.scraperapi.com/

Step 1 - First you need to open accounts in these website and get your API_KEYS  
Step 2 - Configuer the main.py file with your API_KEYS and the amazon product's link you want to check.  
Step 3 - Run the command 'pip install -r requirements.txt'  
Step 3 - Run the scipt by the command 'python3 main.py'

It will keep running untill your product is available and upon availability it will ping you with a call.
For more ease you can also deploy this script in any cloud server like python any where.
