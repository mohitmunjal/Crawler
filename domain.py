from urlparse import urlparse

#example.com last two words
def get_domain_name(url):
    try:
        results=get_sub_domain_name(url).split('.')
        return (results[-2] + '.' + results[-1])
    except:
        return ''

# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
