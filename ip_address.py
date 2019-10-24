import os


def get_Ip_address(url):
    command='nslookup ' + url
    process=os.popen(command)
    results=str(process.read())
    marker=results.find('Address:')+9
    return results[marker:].splitlines()[0]

    #return results
#print(get_Ip_address('facebook.com'))

