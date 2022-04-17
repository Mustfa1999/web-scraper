from web_scraper.scraper import WebScraper
import pytest


def test_get_citations_needed_count(ws):
    assert ws.get_citations_needed_count() == 5
    

def test_get_citations_needed_report(ws):
    ws.get_citations_needed_count()
    for p in ws.citation_needed:
        assert p.count("<p>") == 1


@pytest.fixture
def ws():
    return WebScraper("https://en.wikipedia.org/wiki/History_of_Mexico")
    