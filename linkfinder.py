from HTMLParser import HTMLParser
from urllib import *
from urlparse import urlparse,urljoin

class LinkFinder(HTMLParser):

    #def handle_data(self,data):

    def __init__(self,base_url,page_url):
        HTMLParser.__init__(self)
        self.base_url=base_url
        self.page_url=page_url
        self.links_set=set()

    #When we call HTMLParser feed(),this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        #print tag
        if tag=='a':
            for(attributes, value) in attrs:
                if attributes=='href':
                    url = urljoin(self.base_url,value)
                    #print url
                    self.links_set.add(url)


    def page_links(self):
        return self.links_set

    def error(self,message):
        pass

#finder=LinkFinder('https://thenewboston.com','thenewboston.com')
#finder.feed('<html><head><title>Test</title></head>'
            #'<body><h1>www.ecounsellors.in</h1></body></html>')  #this automaically feeds data to the LinkFinder class
