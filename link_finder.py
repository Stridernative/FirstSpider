from html.parser import HTMLParser
from urllib import parse
from bs4 import BeautifulSoup


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
       # url = 'https://www.apple.com/retail/storelist/' + str(page)
        #source_code = requests.get(url)
       # if tag == ('a', {'class': 'data-store-number'}):
        isStore = False
        storeList = []
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'data-store-number':
                   # print(attrs)
                    isStore = True
                if attribute == 'href' and isStore:
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
                   # print(value)
                    storeList.append('apple.com' + value)
                    isStore = False

            for store in storeList:
                print(store)

    def page_links(self):
        return self.links

    def error(self, message):
        pass