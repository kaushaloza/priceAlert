import requests

from bs4 import BeautifulSoup

# mail protocol:enable u to send emails
import smtplib
userName = input("Enter your name user:")

URL = input("Enter your Link here:")

expectedPrice = int(input("Enter the target price:"))

while(expectedPrice == 0):
    print("Dont joke user enter proper price.")
    expectedPrice = int(input("Enter the target price:"))


userEmail = input("Enter your email:")

while(userEmail == ""):

    print("Email can not be null enter again:")
    userEmail = input("Enter your email:")






headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# return title as text formate
title = soup.find(id="productTitle").get_text()


print(f"Hellow {userName} thank you for using our service, we will send an email when your product {title} is available at {expectedPrice} price.")
def checkPrice():
    price = soup.find(id="priceblock_ourprice").get_text()

    p_price = price.replace(',',"")
    converted_price = float(p_price[1:])

    if(converted_price > expectedPrice):
        sendEmail()

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #establishes the connection
    server.starttls() #encryptes
    server.ehlo()

    server.login('kaushaloza8@gmail.com','uwvudbqsbohbqfzw')

    subject = "Price fall down"
    body = f"Hey {userName} how are you ,You product's price dropped check it out .Check this link: https://www.amazon.in/Sony-Premium-Compact-DSC-RX100M5A-Advanced/dp/B07JZX4J3T/ref=sr_1_9?keywords=sony' \
      '%2Bcamera&qid=1637078802&sr=8-9&th=1"

    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'kaushaloza8@gmail.com',
        userEmail,
        msg

    )
    print("Email has been sent")
    server.quit()

checkPrice()





