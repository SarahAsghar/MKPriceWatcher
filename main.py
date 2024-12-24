import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import DB
import info
from decimal import Decimal

saleXPath = "//*[@id=\"pdp-default\"]/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/h3/span/span[2]/span[2]"
nonSaleXPath = "//*[@id=\"pdp-ugc-3\"]/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/h3/span/span/span[2]"

def main():
    db = DB.DB()
    purses = db.getPurses()
    for data in purses:
        id = data[0]
        link = data[2]
        price = findPrice(link).strip()[1:]
        price = Decimal(price)

        prevPursePrice = db.getLatestPrice(id)
        if len(prevPursePrice) == 0 or price != prevPursePrice[0][1]:
            db.addPrice(id, price)
            pass
        else:
            print("Price is same")

    print(db.getPrices(0))





def findPrice(link):
    browser = webdriver.Safari()
    browser.get(link)

    try:
        price = browser.find_element(By.XPATH, saleXPath).text
    # //*[@id="pdp-ugc-3"]/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/h3/span/span/span[2]

    except:
        price = browser.find_element(By.XPATH, nonSaleXPath).text
    browser.close()
    return price
    

    




if __name__ == '__main__':
    main()








