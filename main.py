import csv # csv reader
import argparse # argument parser

import requests
# imported the urllib library
import urllib

# location of csv containing currencies 
url ="https://focusmobile-interview-materials.s3.eu-west-3.amazonaws.com/Cheap.Stocks.Internationalization.Currencies.csv"
 



# find currency in csv file
def findCurrency(currency):
    # Copy csv to a local file
    urllib.request.urlretrieve(url, "currencies.csv")
    with open("currencies.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:            
            if row[2].lower() == currency:      
                return row
            

# terminal argument parser
def parseArgs():
    # create a parser
    parser = argparse.ArgumentParser(description='Check if currency exists.')
    parser.add_argument("-c", "--currency", help="currency in ISO 4217 Code format.")
    args = parser.parse_args()
    return args


# run code
if __name__ == '__main__':
    args = parseArgs()
    currency = args.currency.lower()
    result = findCurrency(currency)
    if result != None:
        print('Currency available')
    else: 
        print('Currency NOT available')
    