import os
import json
from typing import Optional, Dict, Any, List
import logging

logger = logging.getLogger(__name__)

def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
    return None

def write_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error writing to file {file_path}: {str(e)}")
        return False

def ensure_directory_exists(dir_path: str) -> bool:
    try:
        os.makedirs(dir_path, exist_ok=True)
        return True
    except Exception as e:
        logger.error(f"Error creating directory {dir_path}: {str(e)}")
        return False

def get_file_extension(file_path: str) -> Optional[str]:
    _, ext = os.path.splitext(file_path)
    return ext.lower() if ext else None

def filter_files_by_extension(dir_path: str, extensions: List[str]) -> List[str]:
    if not os.path.isdir(dir_path):
        logger.error(f"Directory not found: {dir_path}")
        return []
    
    matched_files = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            ext = get_file_extension(file)
            if ext in extensions:
                matched_files.append(os.path.join(root, file))
    return matched_files

def validate_email(email: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None