import requests                         #requests module imported in PyCharm
from bs4 import BeautifulSoup           #BeautifulSoup module imported in Pycharm


def core_spider(max_pages):                       #Driver function for the core spider 
    page = 1                                      #initialising page number

    while page <= max_pages:                      #incrementing pages
    
        url = 'https://www.flipkart.com/womens-clothing/lingerie-sleep-swimwear/bras/pr?otracker=nmenu_sub_Women_0_Bras&page=' + str(page) + "&sid=2oq%2Cc1r%2Ctbt%2C3o8&viewType=grid"
        
        
        
        source_code = requests.get(url)           #reuquests module fetches the url and stores it insource_code variable
        plain_text = source_code.text             #stores the retrieved URL as plain text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': "_2cLu-l"}):      #findAll parameters are found by inspecting the page source, 
                                                                  #i.e for headers its the <a> or anchor points and {'class': "_2cLu-l"} that
                                                                  ##was common to all the anchor points for the products displayed in that page
                                                                   
             
             
             
            
            href = "https://www.flipkart.com" + link.get('href')        # only link.get(href) will return only a part of link and that's why
                                                                        #"https://www.flipkart.com" was used to fetch the complete URL
                                                                        
                                                                        
            title = link.string                                        #stores the string part in the written HTML code
            
            
            print(title)                                               #logs title and url to the console
            print(href)
        page += 1


core_spider(2)                                                         #calling the driver function
