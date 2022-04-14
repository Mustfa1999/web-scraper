from web_scraper.scraper import WebScraper


def test_get_citations_needed_count():
    ws = WebScraper("https://en.wikipedia.org/wiki/History_of_Mexico")
    assert ws.get_citations_needed_count() == 5
    


