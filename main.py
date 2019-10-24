from base import*
from domainname import*
from ip_address import *
from nmap import*
from robot_text import *
from whois import *

ROOT_DIR='scans'
create_dir(ROOT_DIR)


def run_scans(name, url):
    domain_name=get_domain_name(url)
    ip=get_Ip_address(domain_name)
    nmap=get_nmap('-F', ip)
    robots_txt=get_robot_text(url)
    whois=get_whois(domain_name)
    save_data(name,url,domain_name,ip,nmap,robots_txt,whois)


def save_data(name,url,domain_name,ip,nmap,robots_txt,whois):
    site_dir=ROOT_DIR + '/' + name
    create_dir(site_dir)
    write_file(site_dir + '/url.txt',url)
    write_file(site_dir) + '/domain.txt',domain_name
    write_file(site_dir + '/ip.txt')
    write_file(site_dir + '/nmap.txt',nmap)
    write_file(site_dir + '/robots_txt',robots_txt)
    write_file(site_dir + '/whois.txt',whois)


run_scans('Facebook', 'https://www.facebook')
