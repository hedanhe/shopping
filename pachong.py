import requests
from bs4 import BeautifulSoup
from lxml import etree

soup = BeautifulSoup(open("./templates/index.html", "r"), 'lxml')
# print(soup.prettify())
html = etree.parse('./templates/index.html', etree.HTMLParser())

result = html.xpath('//a[contains(@class, "detail-text")]/@data-lab')
print(result)
with open('detail-content.txt', "w") as f:
    for i in result:
        f.write(i)
        f.write("\n")