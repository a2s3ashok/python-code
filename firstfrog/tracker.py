import  requests
from bs4 import BeautifulSoup
URL = 'https://www.amazon.in/dp/B00RHUFDZS/ref=s9_acsd_al_bw_c2_x_11_i?pf_rd_m=A1K21FY43GMZF8&pf_' \
      'rd_s=merchandised-search-5&pf_rd_r=9JS917XVW0CR44EGH41D&pf_rd_t=101&pf_rd_p=d0f045d8-be6b-489' \
      '1-ad0e-d27cd2ab1068&pf_rd_i=21345101031'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
       ' Chrome/81.0.4044.122 Safari/537.36' }

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').get_text()
price = soup.find(id='priceblock_ourprice').get_text
converted_price = float(price[0:5])

if (converted_price <1700)
print(converted_price)
print(title.strip())
