import os
import sys
import logging
from dotenv import load_dotenv

# Ensure the project root is in the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Load environment variables
load_dotenv()

from linkedin_tech_news_agent.agent import LinkedInTechNewsAgent
from linkedin_tech_news_agent.credential_manager import SecureCredentialManager

def setup_logging():
    """Configure logging for the application"""
    log_dir = os.path.join(project_root, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(log_dir, 'tech_news_agent.log')),
            logging.StreamHandler()
        ]
    )

def main():
    """Main entry point for the LinkedIn Tech News Agent"""
    try:
        # Setup logging
        setup_logging()
        logger = logging.getLogger(__name__)
        
        # Initialize credential manager
        credential_manager = SecureCredentialManager()
        
        # Initialize and run the agent
        agent = LinkedInTechNewsAgent(credential_manager)
        agent.run()
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)

if __name__ == '__main__':
    main()