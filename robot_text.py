import urllib.request
import io

def get_robot_text(url):
    if url.endswith('/'):
        path=url
    else:
        path=url + '/'
    req=urllib.request.urlopen(path + "robots.txt", data=None)
    data=io.TextIOWrapper(req, encoding='utf-8')
    return data.read()
print(get_robot_text('https://www.google.com/'))
