from urllib import urlopen
import urllib
from urllib2 import *
from linkfinder import LinkFinder
from general import *
from bs4 import BeautifulSoup


class Spider:

    #Class variables(shared among all instances)

    project_name=''
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue=set()
    crawled=set()

    def __init__(self,project_name,base_url,domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file=Spider.project_name + '/queue.txt'
        Spider.crawled_file=Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider',Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name,Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name,page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' is now crawling ' + page_url)
            print('Queue' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            #Now we have updated the sets i.e picked a link from queue, crawled it and stored reults in set
            #Now we need to update files
            Spider.update_files()

    #Connects to site, it takes htm, converts to string and crawls the page
    @staticmethod
    def gather_links(page_url):
        html_string=''
        try:
            #sprint "HY"
            response = urllib.urlopen(page_url)
            html_bytes=urllib.urlopen(page_url).read()
            print html_bytes
            #print "HY"
            #print response.info()
            #makes sure its actually a html file and nothing else
            if response.info().getheader('content-type') == 'text/html':
                print "afhj"
                print html_bytes
                html_string = html_bytes.decode("utf-8")
                print html_string
                finder=LinkFinder(Spider.base_url,page_url)
                finder.feed(html_string)

        except:
            print('Error: can not crawl page')
            return set()
        return finder.page_links()

    #Adding newly crawled links to waiting list i.e queue
    @staticmethod
    def add_links_to_queue(links_set):
        for url in links_set:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            #Facebook wagerah na aa jaye
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)
