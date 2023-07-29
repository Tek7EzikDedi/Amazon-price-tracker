import smtplib
import requests
from bs4 import BeautifulSoup
import lxml
import os


URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = { 'Accept-Language' : "tr-TR,tr;q=0.9",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
response = requests.get(URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "lxml")
price = int(soup.find(class_="a-price-whole").getText().replace(".",""))
sent_price = int(soup.find(class_="a-price-fraction").getText())
title = soup.find(id="productTitle").getText()
print(price)

email = "fatihharsx4@gmail.com"
password = os.environ["password"]

def send_mail(e_mail, text):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=e_mail,
                            msg=f"Subject:Amazon Price Alert!\n\n{text}".encode("UTF-8"))

text = f"{title}\n${price}.{sent_price}\n{URL}"
if price < 100:
    send_mail("fatihhars70@gmail.com", text=text)