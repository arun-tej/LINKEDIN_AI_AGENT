import os
import json
import base64
import logging
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class SecureCredentialManager:
    def __init__(self, config_dir='config'):
        """
        Initialize Secure Credential Manager
        
        :param config_dir: Directory to store credentials
        """
        self.logger = logging.getLogger(__name__)
        self.config_dir = config_dir
        self.credentials_path = os.path.join(config_dir, 'secure_config.json')
        self.key_path = os.path.join(config_dir, 'encryption_key.key')
        
        # Ensure config directory exists
        os.makedirs(config_dir, exist_ok=True)
    
    def _generate_key(self, password):
        """
        Generate encryption key from password
        
        :param password: Master password
        :return: Encryption key
        """
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key, salt
    
    def save_credentials(self, credentials, master_password):
        """
        Save and encrypt credentials
        
        :param credentials: Dictionary of credentials
        :param master_password: Master password for encryption
        """
        try:
            # Generate encryption key
            key, salt = self._generate_key(master_password)
            f = Fernet(key)
            
            # Encrypt credentials
            encrypted_data = f.encrypt(json.dumps(credentials).encode())
            
            # Save encrypted credentials and salt
            with open(self.credentials_path, 'wb') as file:
                file.write(salt + encrypted_data)
            
            self.logger.info("Credentials saved successfully")
        
        except Exception as e:
            self.logger.error(f"Error saving credentials: {e}")
    
    def load_credentials(self, master_password):
        """
        Load and decrypt credentials
        
        :param master_password: Master password for decryption
        :return: Decrypted credentials
        """
        try:
            # Read encrypted data
            with open(self.credentials_path, 'rb') as file:
                data = file.read()
            
            # Extract salt and encrypted data
            salt = data[:16]
            encrypted_data = data[16:]
            
            # Generate key
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
            
            # Decrypt credentials
            f = Fernet(key)
            decrypted_data = f.decrypt(encrypted_data)
            
            return json.loads(decrypted_data.decode())
        
        except FileNotFoundError:
            self.logger.error("Credentials file not found")
        except Exception as e:
            self.logger.error(f"Error loading credentials: {e}")
        
        return None