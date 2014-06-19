import urllib2
from bs4 import BeautifulSoup
url = urllib2.urlopen("http://www.sfgate.com/cgi-bin/listings/restaurants/list?cuisine=Indian&vattr=&loc=&county=&city=&nhood=&orate_min=-1.0&orate_max=4.0&prate_min=1.0&prate_max=4.0&nrate_min=1.0&nrate_max=5.0&year=&term=&Submit=Search&Search=1&Advanced=1&Reservations=&sort=orate&ord=DESC")
content = url.read()
# Get the contents of the website with BeautifulSoup 
soup = BeautifulSoup(content)

# Get the links to all the restaurants 
restaurant = soup.findAll("div", attrs={"class": "item links"})
# Get the nested lists
lists = []
for ul in restaurant:
	for li in ul.findAll("li"):
		lists.append(li)

#Get the hyperlinks within each list: 
links = []
for link in lists:
	links.append(soup.findAll("li", attrs={"class": "first"}))

print links[0]


