from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# open url handle
url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Exercise example
# Retrieve all of the a tags
# tags = soup("a")
# for tag in tags :
#     # look at parts of the tag
#     print("TAG:", tag)
#     print("URL:", tag.get("href", None))
#     print("Contents:", tag.contents[0])
#     print("Attributes:", tag.attrs)

# count up span tags, and sum their contents
count = 0
sum = 0
tags = soup("span")

for tag in tags :
    count += 1 
    sum += int(tag.contents[0])

print(count)
print(sum)