import requests
from bs4 import BeautifulSoup


class WebScraper:
    """
    A class that search for the paragraphs with no citations
    you hae to provid the url when initializing a new object
    """
    
    def __init__(self, url):
        self.url = url
    
    
    def get_citations_needed_count(self):
        """
        count and return the number of citation needed paragraphs 
        """
        
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        paragraphs = soup.find_all('p')
        
        self.citation_needed = []
        
        for p in paragraphs:
            super_scripted = p.find_all('sup')    
            for sup in super_scripted:
                if sup:
                    list_item = sup.find('i')
                    if list_item:
                        anchor = list_item.find('a')
                        self.citation_needed.append(p)
                

        return len(self.citation_needed)

        
        
    def get_citations_needed_report(self):
        """
        reports the citation needed paragraphs in a well-formatted dict with each citation needed in order found
        """
        
        self.get_citations_needed_count()
        
        self.report = {}
        counter = 1

        for text in self.citation_needed:
            self.report[f"Paragraph {counter}: "] = f"{str(text)[3:-4]}"
            counter += 1
            
        return self.report

    
    def save_results(self):
        """
        saves the results in a text file
        """
        
        self.get_citations_needed_report()
        
        with open('citations_needed_report.txt', 'w') as f:
            f.write("Citation needed paragraphs:\n")
            for i, j in self.report.items():
                f.write(f"{str(i)}{str(j)}")
            
    
    
ws = WebScraper("https://en.wikipedia.org/wiki/History_of_Mexico")
ws.get_citations_needed_report()
    