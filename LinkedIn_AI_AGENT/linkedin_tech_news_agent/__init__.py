
"""
LinkedIn Tech News Agent

This package provides an automated solution for scraping and posting 
tech news to LinkedIn.
"""

__version__ = "0.1.0"
__author__ = "Arun Tej"
__email__ = "aruntej.saibabugodavarthi@gmail.com"

# Import key components for easy access
from .agent import LinkedInTechNewsAgent
from .scraper import TechNewsScraper
from .credential_manager import SecureCredentialManager
from .utils import generate_linkedin_post

# Define what should be imported with * 
__all__ = [
    'LinkedInTechNewsAgent',
    'TechNewsScraper',
    'SecureCredentialManager',
    'generate_linkedin_post'
]