from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# ignore cert errors
ctx = ssl.create_default_context()
ctx.check_hostname  = False
ctx.verify_mode = ssl.CERT_NONE

# take user args
url = input("Enter URL: ")
if len(url) == 0:
	url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
	# url = 'http://py4e-data.dr-chuck.net/known_by_Lillyann.html'

name_position = input("Follow which link position on page: ")
if len(name_position) == 0:
	name_position = 3

link_depth = input("Follow links x times: ")
if len(link_depth) == 0:
	link_depth = 4

# start counter
link_count = 0

# open url handle
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a') 


loop_count = 0

for tag in tags:
	loop_count += 1
	print(tag.contents)
	print(tag)

print('done')



