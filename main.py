import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    print()
    

if __name__ == '__main__':
    main()




# url = 'https://www.michaelkors.com/ca/en/greenwich-small-saffiano-leather-crossbody-bag/32S1GGRC0L.html?skuId=785312024&syte_ref=personalization'
url = "https://www.michaelkors.com/ca/en/nolita-large-nubuck-hobo-shoulder-bag/30F4GY5H3T.html?astc=true&dwvar_30F4GY5H3T_color=0220"
browser = webdriver.Safari()
browser.get(url)

try:
 bnum = browser.find_element(By.XPATH, "//*[@id=\"pdp-default\"]/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/h3/span/span[2]/span[2]").text
# //*[@id="pdp-ugc-3"]/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/h3/span/span/span[2]

except:
     bnum = browser.find_element(By.XPATH, "//*[@id=\"pdp-ugc-3\"]/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/h3/span/span/span[2]").text


print(bnum)
browser.close()



