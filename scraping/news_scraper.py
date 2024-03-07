import requests
from parsel import Selector


class NewsScraper:
    PLUS_URL = 'https://www.championat.com'
    URL = 'https://www.championat.com/news/1.html'
    HEADERS = {
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
    }

    LINK_XPATH = '//div[@class="news-item"]/div[@class="news-item__content"]/a/@href'

    def scrape_data(self):

        response = requests.request(method="GET", url=self.URL, headers=self.HEADERS)
        # print(response.text)

        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).extract()

        for link in links:
            print(self.PLUS_URL + link)
        return links


if __name__ == '__main__':
    scraper = NewsScraper()
    scraper.scrape_data()
