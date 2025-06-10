import json
from typing import List, Dict


def select_products(data: List[Dict], theme: str, limit: int = 10) -> List[Dict]:
    """Simple product selection based on theme keyword in title."""
    selected = [p for p in data if theme.lower() in p.get("title", "").lower()]
    return selected[:limit]


def load_products(path: str) -> List[Dict]:
    with open(path, 'r', encoding='utf-8') as fh:
        return json.load(fh)
