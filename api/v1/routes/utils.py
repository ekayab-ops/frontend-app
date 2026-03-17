# utils.py

from datetime import datetime
import hashlib
import os

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def is_production():
    return os.environ.get('NODE_ENV') == 'production'

def get_config():
    config_file = os.path.join(get_project_root(), 'config.json')
    with open(config_file, 'r') as f:
        return json.load(f)