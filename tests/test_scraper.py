from web_scraper.scraper import WebScraper
import pytest


def test_get_citations_needed_count(ws):
    assert ws.get_citations_needed_count() == 5
    

def test_get_citations_needed_report():
    with open('citations_needed_report.txt', 'r') as f:
        assert "".join(f.readlines()).count("<p>") == 5


@pytest.fixture
def ws():
    return WebScraper("https://en.wikipedia.org/wiki/History_of_Mexico")
    