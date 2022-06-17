import csv
import requests
import mysql.connector

# Initialize the database
mydb = mysql.connector.connect(
    host="localhost",
  user="myusername",
  password="mypassword",
  database="mydatabase"
)

# Get the asset data
respToken = requests.get('https://api.kraken.com/0/public/Assets')
# the JSON-data will be changed to a python type = dict
token = respToken.json()

# Get the pair data
respPair = requests.get('https://api.kraken.com/0/public/AssetPairs')
pair = respPair.json()

def getKeys():
    assetInfo = []
    for i in token['result'].keys():
        assetInfo.append(i)
    return assetInfo


def getValues(value):
    valueData = []
    for i in token['result'].keys():
        valueData.append(token['result'][i][value])
    return valueData

def storeToCSV(fileName, key, value, request):
    with open(fileName, 'w') as file:
        writer = csv.writer(file)
        header = ['asset', request]
        writer.writerow(header)
        for i in range(len(key)):
            column = [key[i], value[i]]
            writer.writerow(column)

def wrapper(fileName, value):
    storeToCSV(fileName, getKeys(), getValues(value), value)

if __name__ == '__main__':
    wrapper('Data.csv', 'altname')
    for i in pair['result'].keys():
        print(i)
        print(pair['result'][i]['quote'])