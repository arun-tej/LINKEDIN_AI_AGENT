import os

# Application Configuration
class Config:
    # Project Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOG_DIR = os.path.join(BASE_DIR, 'logs')
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    
    # LinkedIn API Configuration
    LINKEDIN_CLIENT_ID = os.getenv('LINKEDIN_CLIENT_ID', '')
    LINKEDIN_CLIENT_SECRET = os.getenv('LINKEDIN_CLIENT_SECRET', '')
    
    # Scraping Configuration
    SCRAPE_SOURCES = [
        'https://techcrunch.com/category/artificial-intelligence/',
        'https://www.theverge.com/tech',
    ]
    
    # Logging Configuration
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_DIR, 'tech_news_agent.log'),
                'formatter': 'standard',
            },
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': True
            },
        }
    }