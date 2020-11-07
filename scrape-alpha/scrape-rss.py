##imports - add functionality beyond base python.  you might have to do a pip install to get this running https://docs.python.org/3/reference/import.html
import requests # for pulling data https://www.w3schools.com/python/module_requests.asp
# We are not binding the module name, but going through the list of identifiers
from bs4 import BeautifulSoup #https://docs.python.org/2.0/ref/import.html
#import csv # this is to export a csv.  not as useful if this is serverless but a good local export

#create settings area
#rsstarget='https://aws.amazon.com/about-aws/whats-new/recent/feed/'


# original from Corey Schafer https://www.youtube.com/watch?v=ng2o98k983k
#source = requests.get('http://coreyms.com').text

#20201107-1148 do i need this in codeburst.io version?
#soup = BeautifulSoup(source, 'lxml')

# scraping function
def hackernews_rss('https://news.ycombinator.com/rss'):
    try:
        r = requests.get()
        return print('The scraping job succeeded: ', r.status_code)
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)
print('Starting scraping')
hackernews_rss()
print('Finished scraping')