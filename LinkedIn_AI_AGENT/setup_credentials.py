import os
import json
import getpass
from linkedin_tech_news_agent.credential_manager import SecureCredentialManager

def setup_credentials():
    """
    Interactive script to set up credentials securely
    """
    # Ensure config directory exists
    config_dir = 'config'
    os.makedirs(config_dir, exist_ok=True)

    # Initialize credential manager
    credential_manager = SecureCredentialManager(config_dir)

    # Collect LinkedIn API credentials
    print("LinkedIn API Credential Setup")
    client_id = input("Enter LinkedIn Client ID: ")
    client_secret = input("Enter LinkedIn Client Secret: ")

    # Master password for encryption
    while True:
        master_password = getpass.getpass("Create a master password for encryption: ")
        confirm_password = getpass.getpass("Confirm master password: ")
        
        if master_password == confirm_password:
            break
        else:
            print("Passwords do not match. Please try again.")

    # Prepare credentials dictionary
    credentials = {
        "linkedin_client_id": client_id,
        "linkedin_client_secret": client_secret,
        # Add any additional credentials you might need
    }

    # Save encrypted credentials
    try:
        credential_manager.save_credentials(credentials, master_password)
        print("\n✅ Credentials saved successfully!")
        print("Files created:")
        print(f"- {os.path.join(config_dir, 'secure_config.json')}")
        print(f"- {os.path.join(config_dir, 'encryption_key.key')}")
    except Exception as e:
        print(f"❌ Error saving credentials: {e}")

def main():
    setup_credentials()

if __name__ == '__main__':
    main()