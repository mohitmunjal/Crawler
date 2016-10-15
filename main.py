import threading #Each thread is a worker
from Queue import Queue #queue is basically the job to be done
from spider import Spider
from domain import *
from general import *

print 'Enter Project Name'
PROJECT_NAME = raw_input('>')
HOMEPAGE = 'https://www.youtube.com'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
#this is the thread queue or job
queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)
"""
# Create worker threads (will die when main exits)
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):  #We use a _ becaue we just want to loop 8 times
        t = threading.Thread(target=work)
        t.daemon = True #To make sure it dies when main exists
        t.start()

#Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()

#Each queue link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link) # adding in the thread queue
    #this insures that threads don't bump into each other
    queue.join()
    crawl()

# check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print (str(len(queued_links)) +' links in the queue ')
        create_jobs()

create_spiders()
crawl()
"""
