import json
from campaign_ai.product_selector import select_products


def test_select_products():
    data = [
        {"title": "Sommer Stol", "price": "199"},
        {"title": "Køkkenkniv", "price": "299"},
        {"title": "Sommer Parasol", "price": "499"},
    ]
    selected = select_products(data, "Sommer")
    assert len(selected) == 2
    assert selected[0]["title"] == "Sommer Stol"
    assert selected[1]["title"] == "Sommer Parasol"
