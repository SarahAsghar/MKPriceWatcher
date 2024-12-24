import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import DB
import info
from decimal import Decimal

saleXPath = "//*[@id=\"pdp-default\"]/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/h3/span/span[2]/span[2]"
nonSaleXPath = "//*[@id=\"pdp-ugc-3\"]/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/h3/span/span/span[2]"
db = DB.DB()

def main():
    global db
    updatePrice()

def updatePrice():
    global db
    purses = db.getPurses()
    for data in purses:
        id = data[0]
        link = data[2]
        price = findPrice(link)
        if(price != None):
            prevPursePrice = db.getLatestPrice(id)

            if len(prevPursePrice) == 0 or price != prevPursePrice[0][1]:
             db.addPrice(id, price)
            else:
              print("Price is same")

    print(db.getPrices())


def addPurse(name, link):
    global db
    purse = db.getPurseWithLink(link)
    latestID = db.getLatestPurseID()
    id = latestID[0][0] + 1
    if(len(purse) == 0 and id != latestID):
        db.addPurse(id, name, link)
        price = findPrice(link)
        db.addPrice(id, price)
    else:
        print("already in")

    pass


def findPrice(link):
    browser = webdriver.Safari()
    browser.get(link)
    try:
        price = browser.find_element(By.XPATH, saleXPath).text
    except:
        try:
            price = browser.find_element(By.XPATH, nonSaleXPath).text
        except:
            pass
    browser.close()
    if(price != None):
        price = Decimal(price.strip()[1:])
    return price
    

    




if __name__ == '__main__':
    main()








