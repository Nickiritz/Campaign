from campaign_ai.pdf_generator import generate_catalog


def test_generate_catalog(tmp_path):
    products = [
        {"title": "Test", "price": "100", "description": "desc"}
    ]
    output = tmp_path / "out.pdf"
    generate_catalog(products, str(output), "Title")
    assert output.exists() and output.stat().st_size > 0
