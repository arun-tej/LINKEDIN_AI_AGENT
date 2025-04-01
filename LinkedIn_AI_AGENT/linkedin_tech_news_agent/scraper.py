import requests
import logging
import random
import hashlib
from bs4 import BeautifulSoup

class TechNewsScraper:
    def __init__(self):
        """
        Initialize the Tech News Scraper
        """
        self.logger = logging.getLogger(__name__)
        
        # Tech news sources
        self.sources = [
            'https://techcrunch.com/category/artificial-intelligence/',
            'https://www.theverge.com/tech',
            'https://www.wired.com/category/gear/',
            'https://arstechnica.com/gadgets/'
        ]
    
    def _generate_article_hash(self, title, url):
        """
        Generate a unique hash for an article to prevent duplicates
        
        :param title: Article title
        :param url: Article URL
        :return: MD5 hash
        """
        return hashlib.md5((title + url).encode()).hexdigest()
    
    def scrape_tech_news(self, limit=5):
        """
        Scrape tech news from multiple sources
        
        :param limit: Maximum number of articles to scrape
        :return: List of scraped articles
        """
        articles = []
        
        for source in self.sources:
            try:
                # Randomize user agent
                user_agents = [
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
                    'Mozilla/5.0 (X11; Linux x86_64)'
                ]
                
                headers = {
                    'User-Agent': random.choice(user_agents),
                    'Accept-Language': 'en-US,en;q=0.9'
                }
                
                # Fetch webpage
                response = requests.get(source, headers=headers, timeout=10)
                response.raise_for_status()
                
                # Parse HTML
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract articles
                site_articles = soup.find_all(['article', 'div'], class_=['post', 'article'])
                
                for article in site_articles[:limit]:
                    title_elem = article.find(['h2', 'h3'])
                    link_elem = article.find('a')
                    
                    if title_elem and link_elem and link_elem.get('href'):
                        title = title_elem.get_text().strip()
                        url = link_elem.get('href')
                        
                        # Ensure absolute URL
                        if not url.startswith(('http://', 'https://')):
                            url = f"{source.rstrip('/')}/{url.lstrip('/')}"
                        
                        articles.append({
                            'title': title,
                            'url': url,
                            'hash': self._generate_article_hash(title, url),
                            'source': source
                        })
                
                if len(articles) >= limit:
                    break
            
            except requests.RequestException as e:
                self.logger.warning(f"Error scraping {source}: {e}")
        
        return articles