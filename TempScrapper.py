import bs4 as bs
import time
import urllib.request
import requests
from requests.exceptions import HTTPError

#proper error handling for different error code

#Responses can come from https://httpstat.us to verify the error code is taken care of

try:
	source = urllib.request.urlopen('https://www.research.nhg.com.sg/')
	soup = bs.BeautifulSoup(source,'lxml')	
	#print(soup);
	
	print(soup.find_all('a'));
	
	#nav = soup.nav
	#for url in nav.find_all('a'):
	#	print(url.get('href'))
	
	#body = soup.body
	#for paragraph in body.find_all('p'):
	#	print(paragraph.text)

except urllib.error.HTTPError as e: #if
	 #prints the response gracefully. 
	 print(e.code)

print('hello');	

