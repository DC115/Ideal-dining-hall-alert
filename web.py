from bs4 import BeautifulSoup
from smtplib import SMTP
import requests


location_name = {39:"Everyday+Items", 15:"Northwest+Marketplace", '06':"Putnam+Dining+Hall" } #will replace key section with corresponding dining hall key and value
for key, value in location_name.items():
    url = f"https://nutritionanalysis.dds.uconn.edu/shortmenu.aspx?sName=UCONN+Dining+Services&locationNum={key}&locationName={value}&naFlag=1"

    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text,"html.parser")

    menu_items = soup.findAll("div", attrs={"class":"shortmenurecipes"})

    for menu_item in menu_items:
        print(menu_item.text)
