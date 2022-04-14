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
        
        self.citation_needed_paragraphs = []
        
        for p in paragraphs:
            super_scripted = p.find('sup')    
            if super_scripted:
                list_item = super_scripted.find('i')
                if list_item:
                    self.citation_needed_paragraphs.append(p)        
        
        self.citation_needed =[]
        
        for text in self.citation_needed_paragraphs:
            num_of_citations = str(text).count(">citation needed<")
            
            start_point = 0
            for i in range(num_of_citations):
                citation_index = str(text).find(">citation needed<", start_point)
                citation = str(text)[start_point : citation_index+16]
                start_point = citation_index+16
                if citation.count("<p>") == 0:
                    citation = "<p>" + citation[23:]
                self.citation_needed.append(citation)
            
                        
        return len(self.citation_needed)

        
        
    def get_citations_needed_report(self):
        """
        reports the citation needed paragraphs in a well-formatted dict with each citation needed in order found
        """
        
        self.get_citations_needed_count()
        
        self.report = {}
        counter = 1

        for text in self.citation_needed:
            self.report[f"Paragraph {counter}: "] = f"{str(text)}\n"
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
            
    
    
if __name__ == "__main__":
    ws = WebScraper("https://en.wikipedia.org/wiki/History_of_Mexico")
    ws.save_results()
    
