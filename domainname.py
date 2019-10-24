from tld import get_fld

def get_domain_name(url):
    domainname=get_fld(url)
    return domainname
print(get_domain_name('https://www.facebook.com/'))