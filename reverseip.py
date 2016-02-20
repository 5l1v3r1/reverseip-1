# Author :  Hades.y2k
# www.github.com/Hadesy2k
# Date   :  21/Feb/2016
# GPL v<2.0>

import urllib2
import json
import socket
#import random
import sys
import os

def scan(url):
    yougetsignal = "http://domains.yougetsignal.com/domains.php"
    contenttype = "application/x-www-form-urlencoded; charset=UTF-8"

    """useragent_list = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36"\
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"\
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"\
    "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"\
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1"\
    "Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0"\
    "Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1"\
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16"]"""
    useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36" #random.choice(useragent_list)

    postdata = "remoteAddress=" + url + "&key="
    request = urllib2.Request(yougetsignal, postdata)
    request.add_header("Content-type", contenttype)
    request.add_header("User-Agent", useragent)

    try:
        gethost = socket.gethostbyname(url)
        print "[!] Scanning: ", gethost
    except socket.gaierror, e:
        print "[x]", e; exit()

    try:
        result = urllib2.urlopen(request).read()
        parse(json.loads(result))
    except urllib2.HTTPError, e:
        print "[x] Error:" , e.code
    except urllib2.URLError, e:
        print "[x] Error:" , e.args[0][1]

def parse(obj):
    print "[!] Status: " + obj["status"]
    if obj["status"] == "Fail":
        print "[x] Error:  " + obj["message"].split(". ")[0]
        exit()

    print "[+] Domains : " + obj["domainCount"]

    output = open("output.txt", "w")
    for domain, hl in obj["domainArray"]:
        output.write(domain + "\n")
    output.close()
    print "[+] Result is saved as output.txt in current directory"
    print "    Current directory is %s" % os.getcwd()

def help():
    print""">> Usage: python <filename>.py www.site.com
>> www.github.com/Hades.y2k"""
    exit()

class main:
    def __init__(self, url):
        self.url = url
        scan(url)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help': help()
        else: main(sys.argv[1])
    else:
        help()
