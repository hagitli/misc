#running on colab environment, I wrote a simple dynamic html web scarpping script to check the status of our building permit application :)
#basically, we get notification for any increasing on "events" number: "events" considered as new activity on permit status.

#setup
!pip install selenium
!apt-get update 
!apt install chromium-chromedriver

#imports
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver

#settings
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
request_site = ******  #this is the specific URL address of our request
max_num_events = 19 #here we set the max number of events that we are interested on
driver.get(request_site)
html = driver.page_source
soup = BeautifulSoup(html)
results = soup.find(id="events")
spans = results.find_all("span")
my_spn = str(spans[1]).split(sep="(")[1].split(sep=")")[0]

if (int(my_spn) > max_num_events):
  print("got an update! current updates are:",my_spn)
  #or do something else
