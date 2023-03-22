from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup

# ignore cert errors
ctx = ssl.create_default_context()
ctx.check_hostname  = False
ctx.verify_mode = ssl.CERT_NONE

# parameters

# drop this line in to get into debugger
# import pdb; pdb.set_trace()
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# name_position = 3
# link_depth = 4
url = 'http://py4e-data.dr-chuck.net/known_by_Lillyann.html'
name_position = 18
link_depth = 7

# start counter
link_count = 0

# open url handle
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

loop_count = 0

while True:
    print(url)
    if loop_count >= link_depth:
        print(f"breaking after {loop_count} cycles - exceeded limit")
        break
    else:
        # open url an dget tags
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')  
        tag = soup('a')[name_position - 1]
        # print(tag.get('href', None))
        url = tag.get('href', None)
        loop_count += 1


# exploration - how to extract information
# for tag in tags:
#     loop_count += 1
#     print(tag)
#     print(tag.get('href', None))
#     print(tag.contents[0])
#     print(tag.attrs)
#     print(tag.attrs['href'])

# for tag in tags:
#     loop_count += 1
#     if loop_count == name_position:
#         url = tag.get('href', None)
#         html = urlopen(url, context=ctx).read()
#         soup = BeautifulSoup(html, 'html.parser')
#         tags = soup('a')

print('done')