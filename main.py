from twilio.rest import Client
from random import randint
from time import sleep
from bs4 import BeautifulSoup
from scraper_api import ScraperAPIClient


# To BE CONFIGURED BY THE USER -->

# Amazon URL of the product.
URL = "URL OF THE PRODUCT YOU WANT TO CHECK"

# Api key provided by scraperapi.com
scraper_api_key = 'YOUR API_KEY OF SCRAPER API'

# twilio account_sid
account_sid = 'YOUR TWILIO ACCOUNT_SID'

# twilio auth_token
auth_token = 'YOUR TWILIO AUTHENTICATION TOKEN'

# call to
to = 'THE NUMBER YOU WANT TO PING (you have to verify this number in your twilio account first)'

# call from number will be provided by twilio.
from_ = 'THE NUMBER FROM WHICH YOU WANT TO MAKE THE CALL (this will be provided by twilio)'


# Defining required functions.
def check_availability(URL, scraper_api_key):
    sleep(randint(30, 40))
    client = ScraperAPIClient(scraper_api_key)
    result = client.get(URL)

    parsed_html = BeautifulSoup(result.content, 'html.parser')

    availability = parsed_html.select("#availability")

    if availability:

        availability = availability[0].getText().strip().splitlines()[0]

        if availability != "Currently unavailable.":
            return True

    return False


def make_call(account_sid, auth_token, to, from_):
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        to, from_, url='http://demo.twilio.com/docs/voice.xml')


# Code for execution.
if __name__ == "__main__":

    try:
        print("Checking for availability...")
        while True:
            if check_availability(URL, scraper_api_key):
                print("Product available.\nNotifying you with a call...")
                make_call(account_sid, auth_token, to, from_)
                break

            print("Product not available, checking again...")
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
    except Exception as e:
        print("Some error occurred...")
        print(f"Error info: {e}")
