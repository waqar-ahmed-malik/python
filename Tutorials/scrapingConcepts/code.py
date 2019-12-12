from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import csv
import random
from selenium import webdriver


def get_proxy_list():
    ua = UserAgent()
    soup = None
    while soup is None:
        proxies_status_code = 100
        while proxies_status_code != 200:
            try:
                response = requests.get('https://www.sslproxies.org/', headers={'User-Agent': ua.random}, timeout=(10, 10))
                proxies_status_code = response.status_code
                soup = BeautifulSoup(response.content, 'lxml')
                response.close()
            except Exception as e:
                print(e)
                continue
    soup = BeautifulSoup(soup.prettify(), 'lxml')
    soup = soup.find(id='proxylisttable')
    soup = soup.find('tbody')
    return [{"https": "https://" + row.findAll('td')[0].string.strip() + ":" + row.findAll('td')[1].string.strip()}
            for row in soup.findAll('tr') if row.findAll('td')[4].string.strip() == 'elite proxy']


def get_soup_using_requests(url, proxies_list):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    soup = None
    while soup is None:
        if len(proxies_list) == 0:
            proxies_list = get_proxy_list()
        else:
            for proxy in proxies_list:
                try:
                    session = requests.Session()
                    response = session.get(url, headers=headers, proxies=proxy, timeout=(10, 10))
                except:
                    proxies_list.remove(proxy)
                    continue
                soup = response.content
                soup = BeautifulSoup(soup, 'lxml')
                soup = BeautifulSoup(soup.prettify(), 'lxml')
                response.close()
                if soup.text.strip().find('It seems there is some technical issue with your request.') != -1 \
                        or soup.text.strip().upper().find('SUSPICIOUS ACTIVITY DETECTED') != -1:
                    proxies_list.remove(proxy)
                    response.close()
                    print('Blocked')
                    soup = None
                    continue
    if soup is None:
        get_soup_using_requests(url, proxies_list)
    else:
        return soup, proxies_list


def get_soup_using_selenium(url):
    soup = None
    while soup is None:
        try:
            chrome = webdriver.Chrome()
            chrome.get(url)
            soup = chrome.page_source
            soup = BeautifulSoup(soup, 'lxml')
            soup = BeautifulSoup(soup.prettify(), 'lxml')
            chrome.close()
            return soup
        except Exception as e:
            print(e)
            if 'chrome' in locals() or 'chrome' in globals():
                chrome.close()
            continue


def remove_processed_links():
    processed_rows = []
    unprocessed_rows = []
    with open('Processed_Links.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            if len(line) != 0:
                processed_rows.append(line[0])

    if len(processed_rows) == 0:
        return

    with open('Unprocessed_Links.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            if line[0] in processed_rows:
                continue
            else:
                unprocessed_rows.append(line[0])

    with open('Unprocessed_Links.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        for row in unprocessed_rows:
            csv_writer.writerow([row])


def get_links_count():
    remove_processed_links()
    with open('Unprocessed_Links.csv', 'r') as f:
        csv_reader = csv.reader(f)
        return len(list(csv_reader))


def get_links_batch(batch_length):
    remove_processed_links()
    links = []
    with open('Unprocessed_Links.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            links.append(line[0])
            if len(links) > batch_length:
                break
    return links
